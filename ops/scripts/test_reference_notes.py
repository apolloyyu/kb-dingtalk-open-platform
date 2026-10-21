"""Source excerpts must remain scoped, live, unambiguous, and verbatim."""
import importlib.util
import json
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("reference_notes", ROOT / "bin/reference_notes.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ReferenceNotesTest(unittest.TestCase):
    def test_all_curated_quotes_exist_once(self):
        docs = [json.loads(x) for x in (ROOT / "meta/documents.jsonl").read_text().splitlines()]
        _, errors = mod.expand(ROOT, "", docs, validate=True)
        self.assertEqual([], errors)

    def test_current_boundaries_and_evidence(self):
        cases = [
            ("应用机器人Stream模式为什么有webhook", ["sessionWebhook", "Outgoing", "消息接收地址"]),
            ("机器人如何回复并@提问者", ["暂不支持 @", "senderStaffId", "atUserIds"]),
            ("主部门接口怎么调用", ["sys00-mainDeptId", "appAgentId", "userIdList"]),
            ("bpms_task_change 转交被转交人", ["HTTP Method | GET", "任务处理人"]),
            ("审批评论撤回附件下载失败", ["withCommentAttatchment", "暂不支持获取下载链接"]),
            ("PC上传Excel附件", ["image：图片", "video：视频", "audio：音频", "历史文档"]),
        ]
        for query, expected in cases:
            p = subprocess.run(["python3", str(ROOT / "bin/dkdoc"), "ctx", query], capture_output=True, text=True)
            self.assertEqual(0, p.returncode, p.stderr)
            supplement = p.stdout.split("== 补充原文摘录", 1)[-1]
            for word in expected:
                self.assertIn(word, supplement, query)
        for query in ["Stream视频会议直播", "Webhook网络回调超时", "卡片的审批任务转交", "JSAPI获取设备信息"]:
            docs = [json.loads(x) for x in (ROOT / "meta/documents.jsonl").read_text().splitlines()]
            self.assertEqual(("", []), mod.expand(ROOT, query, docs), query)

    def test_stale_or_ambiguous_quote_never_becomes_evidence(self):
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            (root / "notes").mkdir()
            (root / "notes/a.md").write_text('match_all: ["example"]\n{{quote: a | answer}}')
            (root / "a.md").write_text('answer\nanswer\n')
            docs = [{"slug": "a", "local_path": "a.md", "title": "A", "source_url": "https://example.com/a"}]
            output, errors = mod.expand(root, "example", docs)
            self.assertTrue(errors)
            self.assertNotIn("source_url:", output)
            (root / "a.md").write_text('changed\n')
            _, errors = mod.expand(root, "example", docs)
            self.assertTrue(errors)

    def test_real_section_hierarchy_excludes_example_headings(self):
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            (root / "notes").mkdir()
            (root / "notes/a.md").write_text('match_all: ["example"]\n{{quote: a | unique-field}}')
            (root / "a.md").write_text('# Page\n## Type\n#### Text payload\n```markdown\n## Fake example\n```\n| unique-field | required |\n')
            docs = [{"slug": "a", "local_path": "a.md", "title": "A", "source_url": "https://example.com/a"}]
            output, errors = mod.expand(root, "example", docs)
            self.assertEqual([], errors)
            self.assertIn('Type / Text payload', output)
            self.assertNotIn('Fake example', output)


if __name__ == "__main__":
    unittest.main()
