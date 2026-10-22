"""Offline declaration-first selection: exact tables, scope, and example paths."""
import pathlib
import re
import runpy
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'bin'))
import evidence_sections as evidence
DOC = runpy.run_path(str(ROOT / 'bin/dkdoc'), run_name='declaration_tests')

CREATE = ROOT / 'docs/01-应用开发/02-4a8AMF6u2A-服务端-API/0054-user-information-creation.md'
GET = ROOT / 'docs/01-应用开发/02-4a8AMF6u2A-服务端-API/0055-query-user-details.md'
PROBE = '下面是待填写的请求示例，不要实际调用：{"userid":"<USER_ID>","name":"<NAME>"}。userid 与员工工号是同一字段吗？'


def ctx(question, *, full=False):
    result = subprocess.run([sys.executable, str(ROOT / 'bin/dkdoc'), 'ctx', *(['--full'] if full else []), question],
                            text=True, capture_output=True, timeout=30)
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)
    return result.stdout


class DeclarationSelectionTest(unittest.TestCase):
    def test_two_real_request_tables_keep_distinct_required_values_and_scope(self):
        for path, required in ((CREATE, '否'), (GET, '是')):
            with self.subTest(path=path.name):
                source = path.read_text()
                expected = next(part for part in evidence.units(source)
                                if part['scope'] and part['scope'][-1] == '### **请求体**')['body']
                text, status = evidence.select(source, PROBE, 3500, prefer_declarations=True)
                self.assertIn(expected, text)
                self.assertIn('| userid | String | ' + required + ' |', text)
                self.assertIn('## **请求**\n### **请求体**', text)
                self.assertLessEqual(len(text), 3500)
                self.assertFalse(status['overflow'])

    def test_ctx_contains_both_original_required_rows_and_source_urls(self):
        text = ctx(PROBE)
        create = text.split('== 正文[1/', 1)[1].split('== 正文[2/', 1)[0]
        get = text.split('== 正文[2/', 1)[1].split('== 正文[3/', 1)[0]
        self.assertIn('| userid | String | 否 |', create)
        self.assertIn('| userid | String | 是 |', get)
        self.assertIn('| job\\_number | String | 否 |', create)
        self.assertIn('https://open.dingtalk.com/document/development/user-information-creation', create)
        self.assertIn('https://open.dingtalk.com/document/development/query-user-details', get)
        self.assertLessEqual(len(text.rstrip('\n')), 20000)

    def test_nearby_field_questions_keep_full_original_rows(self):
        for question, field in [('创建用户 mobile 字段是否必填', 'mobile'),
                                ('创建用户 job_number 字段是什么意思', 'job\\_number'),
                                ('创建用户 manager_userid 参数如何填写', 'manager\\_userid')]:
            with self.subTest(question=question):
                text, status = evidence.select(CREATE.read_text(), question, 3500, prefer_declarations=True)
                row = next(line for line in CREATE.read_text().splitlines() if line.startswith('| ' + field + ' |'))
                self.assertIn(row, text)
                self.assertLessEqual(len(text), 3500)

    def test_default_selector_keeps_existing_example_selection(self):
        source = GET.read_text()
        for question in ('查询用户详情 Java 请求示例', '查询用户详情接口如何调用', PROBE):
            text, status = evidence.select(source, question, 3500)
            self.assertEqual((text, status), evidence.select(source, question, 3500, prefer_declarations=False))
            if '请求示例' in question:
                self.assertIn('### **请求示例**', text)
                self.assertIn('OapiV2UserGetRequest', text)
            else:
                self.assertIn('查询用户详情', text)

    def test_existing_how_to_example_request_keeps_example_path(self):
        text = ctx('https://open.dingtalk.com/document/development/query-user-details 如何调用？给出 Java 请求示例代码和字段说明')
        self.assertIn('### **请求示例**', text)
        self.assertIn('OapiV2UserGetRequest', text)

    def _assert_mixed_example(self, question):
        intent = DOC['_intent']([question])
        self.assertNotIn('example', intent)
        self.assertTrue(intent['semantic'])
        expected = next(code for code in re.findall(r'```\n(.*?)\n```', CREATE.read_text(), re.S)
                        if 'OapiV2UserCreateRequest' in code)
        text = ctx(question)
        first = text.split('== 正文[1/', 1)[1].split('== 正文[2/', 1)[0]
        self.assertIn('### **请求示例**', first)
        self.assertIn(expected, first)
        self.assertIn('https://open.dingtalk.com/document/development/user-information-creation', first)
        self.assertLessEqual(len(text.rstrip('\n')), 20000)

    def test_mixed_how_to_example_and_parameter_request_keeps_complete_code(self):
        self._assert_mixed_example('https://open.dingtalk.com/document/development/user-information-creation 如何调用？给出 Java 示例代码和 userid 参数说明')

    def test_mixed_how_to_variant_and_parameter_request_keeps_complete_code(self):
        self._assert_mixed_example('https://open.dingtalk.com/document/development/user-information-creation 怎样调用？给出Java示例+userid参数说明')

    def test_explicit_full_fallback_preserves_complete_java_example(self):
        question = 'https://open.dingtalk.com/document/development/user-information-creation 给出 Java 示例代码和 userid 参数说明'
        expected = next(code for code in re.findall(r'```\n(.*?)\n```', CREATE.read_text(), re.S)
                        if 'OapiV2UserCreateRequest' in code)
        self.assertIn(expected, ctx(question, full=True))

    def test_three_code_regressions_share_budget_with_original_field_row(self):
        url = 'https://open.dingtalk.com/document/development/user-information-creation'
        cases = [(url + ' 给出 Java 示例代码和 userid 参数说明', True),
                 (url + ' 给出 Java 示例代码，说明 userid 参数是否必填', False),
                 (url + ' 给出 Java 请求示例和字段说明，我的参数是 {"userid":"001"}', False)]
        source = CREATE.read_text()
        code = next(block for block in evidence._captioned_codes(source, 'Java') if 'OapiV2UserCreateRequest' in block['body'])
        for question, force_full in cases:
            with self.subTest(question=question):
                selected, status = evidence.select(source, question, 3500, prefer_declarations=True)
                self.assertIn(code['body'], selected)
                self.assertIn('| userid | String | 否 |', selected)
                self.assertIn('## **请求**\n### **请求体**', selected)
                self.assertLessEqual(len(selected), 3500)
                self.assertEqual(status['coverage'], 'excerpt')
                text = ctx(question, full=force_full)
                first = text.split('== 正文[1/', 1)[1].split('== 正文[2/', 1)[0]
                self.assertIn(code['body'], first)
                self.assertIn('| userid | String | 否 |', first)
                self.assertLessEqual(len(text.rstrip('\n')), 20000)

    def test_code_caption_and_fence_info_are_dynamic_exact_source_slices(self):
        captioned = 'ImaginaryLang\r\n\r\n```\r\n  complete();  \r\n```\r\n'
        source = '# API\r\n\r\n## Example\r\n\r\n' + captioned
        code = evidence._captioned_codes(source, 'ImaginaryLang')[0]
        self.assertEqual(code['body'], captioned)
        self.assertEqual(code['line'], 5)
        self.assertEqual(code['scope'], ['# API', '## Example'])
        fenced = '# API\n```CustomDSL\n  complete();\n```\n'
        self.assertEqual(evidence._captioned_codes(fenced, 'CustomDSL')[0]['body'], fenced.split('\n', 1)[1])
        self.assertEqual(evidence._captioned_codes(source, 'fields only'), [])

    def test_incomplete_or_ambiguous_code_boundary_cannot_reserve_budget(self):
        self.assertEqual(evidence._captioned_codes('# API\nJava\n```\nunfinished()', 'Java'), [])
        self.assertEqual(evidence._captioned_codes('# API\nJava example and notes\n```\nbody\n```', 'Java'), [])
        body = '# API\nJava\n````\n```not a close\nstill code\n````\n'
        self.assertEqual(evidence._captioned_codes(body, 'Java')[0]['body'], body.split('\n', 1)[1])

    def test_safe_prefix_stops_before_every_unknown_or_container_type(self):
        head = '| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n'
        first = '| target | String | exact [link](https://example.invalid/a) and condition |\n'
        for boundary in ('Object', 'Array', 'CustomType[]', 'Json', 'UnknownType'):
            part = {'scope': ['# API', '## 请求', '### 请求体'], 'line': 4,
                    'body': 'Only condition A.\n\n' + head + first + '| container | ' + boundary + ' | parent |\n'
                            + '| child | String | nested target |\n\nAlso condition B.\n'}
            with self.subTest(boundary=boundary):
                projected = evidence._scalar_prefix_projection(part, 'target 字段')
                self.assertIn(first, projected['body'])
                self.assertTrue(projected['body'].startswith('Only condition A.\n\n'))
                self.assertTrue(projected['body'].endswith('Also condition B.\n'))
                self.assertNotIn('| child |', projected['body'])
                self.assertIsNone(evidence._scalar_prefix_projection(part, 'child 字段'))
                unknown_parent = {**part, 'scope': ['# API', '## Parent object fields']}
                self.assertIsNone(evidence._scalar_prefix_projection(unknown_parent, 'target 字段'))

    def test_projection_is_used_only_when_full_table_and_code_do_not_fit(self):
        table = '| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n| target | String | required qualifier |\n'
        code = 'InventedLang\n\n```\ncomplete()\n```\n'
        source = '# API\n## 请求\n### 请求体\n' + table + '### Example\n' + code + '\n## Noise\n' + 'other\n' * 100
        selected, _ = evidence.select(source, 'InventedLang target 字段', 450, prefer_declarations=True)
        self.assertIn(table.rstrip('\n'), selected)
        self.assertIn(code, selected)
        self.assertNotIn('表格摘录', selected)
        self.assertLessEqual(len(selected), 450)

    def test_table_and_code_in_same_section_are_not_duplicated(self):
        source = '# API\n## 请求体\n| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n| target | String | qualifier |\n'
        source += '\nInventedLang\n\n```\ncomplete()\n```\n\n## Noise\n' + 'other\n' * 100
        selected, _ = evidence.select(source, 'InventedLang target 字段', 400, prefer_declarations=True)
        self.assertEqual(selected.count('complete()'), 1)
        self.assertEqual(selected.count('| target | String | qualifier |'), 1)

    def test_unknown_parent_cannot_be_promoted_over_complete_captioned_code(self):
        table = '| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n| parent | UnknownType | parent object |\n'
        table += ''.join('| other' + str(i) + ' | String | nested |\n' for i in range(140))
        table += '| target | String | child within parent |\n'
        code = 'Java\n\n```\n// target 字段 Java\n' + 'call();\n' * 420 + '```'
        source = '# API\n## 请求\n### 请求体\n' + table + '\n### 请求示例\n' + code
        actual = evidence.select(source, 'Java target 字段', 3500, prefer_declarations=True)
        baseline = evidence.select(source, 'Java target 字段', 3500)
        self.assertEqual(actual, baseline)
        self.assertIn(code, actual[0])
        self.assertNotIn('| target | String |', actual[0])
        self.assertLessEqual(len(actual[0]), 3500)

    def test_opt_in_projection_defers_unknown_type_table_without_orphan_rows(self):
        for type_name in ('UnknownType', 'CustomType[]', 'Json', 'Object', 'Array'):
            table = '| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n| parent | ' + type_name + ' | parent |\n'
            table += ''.join('| other' + str(i) + ' | String | nested |\n' for i in range(30))
            table += '| target | String | nested child |\n'
            with self.subTest(type_name=type_name):
                projected = evidence.project(table, 'target 字段', 300, prefer_declarations=True)
                self.assertIn('表格未展开', projected)
                self.assertNotIn('| target |', projected)
                self.assertFalse(evidence._declaration_match(projected, 'target 字段'))
                text, status = evidence.select('# API\n## 请求\n### 请求体\n' + table,
                                               'target 字段', 300, prefer_declarations=True)
                self.assertNotIn('| target |', text)
                self.assertNotEqual(status['coverage'], 'full')

    def test_projection_checks_type_column_not_field_name(self):
        for field_name in ('UnknownType', 'Object', 'Array'):
            table = '| 类型 | 名称 | 描述 |\n| --- | --- | --- |\n'
            row = '| String | ' + field_name + ' | literal scalar field name |'
            table += row + '\n' + ''.join('| String | other' + str(i) + ' | unrelated |\n' for i in range(30))
            projected = evidence.project(table, field_name + ' 字段', 300, prefer_declarations=True)
            self.assertIn(row, projected)

    def test_supplied_payload_fragments_keep_both_original_required_tables(self):
        question = '请求片段：{"userid":"<USER_ID>","name":"<NAME>"}。userid 与员工工号是同一字段吗？'
        text = ctx(question)
        create = text.split('== 正文[1/', 1)[1].split('== 正文[2/', 1)[0]
        get = text.split('== 正文[2/', 1)[1].split('== 正文[3/', 1)[0]
        self.assertIn('| userid | String | 否 |', create)
        self.assertIn('| userid | String | 是 |', get)

    def test_no_new_example_intent_or_parser(self):
        self.assertNotIn('_example_request', DOC)
        self.assertNotIn('_HOW_TO_RE', DOC)
        for question in (PROBE, '给出Java示例+userid参数说明', '不要只看示例。' + PROBE):
            self.assertNotIn('example', DOC['_intent']([question]))

    def test_negative_narration_and_punctuation_keep_original_required_tables(self):
        for prefix in ('不要只看示例。', '无需生成代码。', '我提供了如下示例。',
                       '只看字段声明，示例代码不需要。', '只看字段声明\n示例代码不需要。'):
            with self.subTest(prefix=prefix):
                text = ctx(prefix + PROBE)
                create = text.split('== 正文[1/', 1)[1].split('== 正文[2/', 1)[0]
                get = text.split('== 正文[2/', 1)[1].split('== 正文[3/', 1)[0]
                self.assertIn('| userid | String | 否 |', create)
                self.assertIn('| userid | String | 是 |', get)

    def test_header_scope_or_fake_example_table_cannot_trigger_priority(self):
        unrelated = '| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n| other | String | unrelated |'
        self.assertFalse(evidence._declaration_match(unrelated, 'target 字段'))
        linked = unrelated.replace('unrelated', '[reference](https://example.invalid/docs)')
        self.assertFalse(evidence._declaration_match(linked, 'https://example.invalid/docs target 字段', ['https', 'example']))
        self.assertFalse(evidence._declaration_match('```markdown\n' + unrelated.replace('other', 'target') + '\n```', 'target 字段'))
        self.assertFalse(evidence._declaration_match('| target | example |\n| --- | --- |\n| value | text |', 'target 字段'))

    def test_nested_deferred_table_does_not_displace_real_small_request_table(self):
        small = '| 名称 | 类型 | 是否必填 | 描述 |\n| --- | --- | --- | --- |\n| target | String | 是 | required identifier |'
        source = '# API\n## Request\n' + small + '\n## Response\n'
        source += '| 名称 | 类型 | 描述 |\n| --- | --- | --- |\n| parent | Object | object |\n'
        source += ''.join('| child' + str(n) + ' | String | target nested data |\n' for n in range(50))
        text, status = evidence.select(source, 'target 字段', 260, prefer_declarations=True)
        self.assertIn(small, text)
        self.assertIn('## Request', text)
        self.assertNotIn('| child', text)
        self.assertNotEqual(status['coverage'], 'full')
        self.assertLessEqual(len(text), 260)

    def test_safe_scalar_table_projection_keeps_header_and_whole_rows(self):
        table = '| 名称 | 类型 | 是否必填 | 描述 |\n| --- | --- | --- | --- |\n'
        table += ''.join('| item' + str(n) + ' | String | 否 | unrelated |\n' for n in range(50))
        target = '| target | String | 是 | complete qualification and source https://example.invalid/a |'
        source = '# API\n## Request\n' + table + target + '\n'
        text, status = evidence.select(source, 'target 字段', 300, prefer_declarations=True)
        self.assertIn(target, text)
        self.assertIn('| 名称 | 类型 | 是否必填 | 描述 |', text)
        self.assertIn('表格摘录', text)
        self.assertEqual(status['coverage'], 'excerpt')
        self.assertLessEqual(len(text), 300)


if __name__ == '__main__':
    unittest.main()
