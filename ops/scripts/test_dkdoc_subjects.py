#!/usr/bin/env python3
"""主体路由与关键证据回归；零模型、零网络，不将检索命中当作答题评分。"""
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]


def ctx(query):
    p = subprocess.run(["python3", str(ROOT / "bin/dkdoc"), "ctx", query],
                       capture_output=True, text=True, timeout=30)
    if p.returncode:
        raise AssertionError(p.stderr or p.stdout)
    return p.stdout


class SubjectEvidenceTest(unittest.TestCase):
    def test_external_assistant(self):
        for q in ("我自己开发的APP，可以把钉钉AI助手连过来吗", "自有App如何集成钉钉AI助理"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertRegex(out, r"== 正文\[1/\d+\] 智能体开发")
                self.assertIn("api-assistantresponse", out)
                self.assertNotIn("== 正文[1/1] 搜索第三方火车票", out)

    def test_monthly_quota(self):
        for q in ("钉钉标准版和专业版调用接口一个月分别多少次限额", "企业内部应用每月API调用额度怎么计算"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertRegex(out, r"== 正文\[1/\d+\] 计费模型说明")
                self.assertRegex(out, r"2025\s*年\s*11\s*月\s*19\s*日")
                self.assertIn("5000", out.replace(",", ""))
                self.assertIn("专业版", out)

    def test_notable_crud_contracts(self):
        for q in ("我想要将一个html界面的后端用钉钉多维表格作为数据库，可能实现吗？",
                  "AI表格可以作为网页后端做增删改查吗"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertRegex(out, r"== 正文\[1/\d+\] 列出多行记录")
                base = "https://api.dingtalk.com/v1.0/notable/bases/{baseId}/sheets/{sheetIdOrName}/records"
                for method, suffix in (("POST", ""), ("PUT", ""), ("POST", "/delete")):
                    self.assertIn(f"{method} {base}{suffix}", out)
                self.assertNotIn("== 正文[1/2] 表达式", out)

    def test_announcement_attachment_subject(self):
        for q in ("公告接口支持附件吗？", "创建企业公告可以携带文件吗"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertRegex(out, r"== 正文\[1/\d+\] 创建公告")
                self.assertIn("获取公告钉盘空间信息", out)
                self.assertIn("发公告时可携带附件信息", out)
                self.assertNotRegex(out, r"== 正文\[1/\d+\] 下载审批附件")

    def test_font_size_keeps_both_platform_matrices(self):
        for q in ("怎么获取钉钉应用配置的字号", "H5如何获取用户设置的字体大小"):
            with self.subTest(q=q):
                out = ctx(q)
                self.assertIn("https://open.dingtalk.com/document/development/jsapi-get-system-info ·", out)
                self.assertIn("https://open.dingtalk.com/document/development/jsapi-get-system-info-sync ·", out)
                self.assertIn("fontSizeSetting", out)
                self.assertIn("H5", out)

    def test_explicit_url_remains_first(self):
        out = ctx("https://open.dingtalk.com/document/development/jsapi-get-system-info-sync 字号字段如何使用")
        first = next(l for l in out.splitlines() if l.startswith("== 正文[1/"))
        self.assertIn("getSystemInfoSync", first)


if __name__ == "__main__":
    unittest.main()
