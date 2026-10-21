#!/usr/bin/env python3
"""Offline product-scope/provenance checks; no model or network."""
import pathlib,sys,unittest,tempfile,json
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'bin'))
import peer_products,evidence_sections
class ProductEvidenceTest(unittest.TestCase):
 def test_scope_and_original_source(self):
  with tempfile.TemporaryDirectory() as temp:
   root=pathlib.Path(temp);(root/'graph').mkdir()
   row={'product':'table','product_title':'示例表格命令参考','title':'字段权限',
        'body':'# 字段权限\n示例产品提供字段权限。','source_url':'https://example.invalid/fixed/source',
        'source_file':'table.md','source_commit':'a'*40}
   other={**row,'product':'calendar','product_title':'日历命令参考','title':'日历','body':'# 日历\n日历原文。','source_file':'calendar.md'}
   (root/'graph/peer-products.json').write_text(json.dumps({'documents':[row,other]}))
   out=peer_products.excerpt(root,'示例表格字段权限怎么设置')
   self.assertIn(row['body'],out);self.assertIn(row['source_url'],out)
   self.assertIn(row['body'],peer_products.excerpt(root,'示例表格字段权限参考 https://example.com/help'))
   poisoned=peer_products.excerpt(root,'示例表格字段权限参考 https://example.com/calendar')
   self.assertIn(row['body'],poisoned);self.assertNotIn(other['body'],poisoned)
   self.assertIn(row['body'],peer_products.excerpt(root,'示例表格字段权限参考 http://example.com/help'))
   for q in ['示例表格API字段权限','示例表格接口字段权限','示例表格SDK字段权限']:
    self.assertEqual(peer_products.excerpt(root,q),'')
 def test_time_provenance_preserves_unknown_and_user_correction(self):
  h='用户：{"refresh_expires_at":"2026-08-01T10:00:00+08:00"}\n助理：{"refresh_expires_at":"2099-01-01T00:00:00Z"}'
  x=json.loads(evidence_sections.time_fields('当时发生了什么',h).split('\n',1)[1])
  self.assertEqual(x['execution_time']['status'],'not_extracted');self.assertEqual(len(x['timestamp_fields']),1)
  x=json.loads(evidence_sections.time_fields('执行时间是2026-07-01 12:00:00+08:00',h).split('\n',1)[1])
  self.assertEqual(x['execution_time']['candidates_from_current_question'],['2026-07-01 12:00:00+08:00'])
 def test_timestamp_literal_zone_fraction_and_date_only(self):
  history='用户：{"refresh_expires_at":"2026-08-10T00:00:00Z"}\n助理：无'
  for value in ['2026-08-01T10:00:00Z','2026-08-01T10:00:00.123456Z','2026-08-01 10:00:00+08:00']:
   x=json.loads(evidence_sections.time_fields('执行时间是'+value,history).split('\n',1)[1])
   self.assertEqual(x['execution_time']['candidates_from_current_question'],[value])
  x=json.loads(evidence_sections.time_fields('执行日期是2026-08-01',history).split('\n',1)[1])
  self.assertEqual(x['execution_time']['status'],'not_extracted');self.assertEqual(x['execution_time']['literal_candidates_with_origin'][0]['value'],'2026-08-01')
 def test_budget_retains_or_defers_complete_json(self):
  data=json.dumps([{'expires_at':'2026-08-01T10:00:00Z'}]*180)
  out=evidence_sections.pack_groups(['== 输入时间字段 ==\n'+data,'== 证据契约 ==\nruntime_observed: no','== 正文[1/1] Example (docs/x.md) ==\nsource_url: https://example.invalid/x'],900)
  self.assertLessEqual(len(out),900);self.assertIn('runtime_observed: no',out)
  self.assertNotIn(data[:60],out);self.assertIn('未展开完整单元',out)
if __name__=='__main__':unittest.main()
