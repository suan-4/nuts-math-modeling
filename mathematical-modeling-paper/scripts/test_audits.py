import importlib.util
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile


HERE = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TextAuditTests(unittest.TestCase):
    def test_real_ai_declaration_is_not_a_placeholder(self):
        module = load("audit_text")
        findings = module.audit_text("AI工具使用声明\n使用ChatGPT辅助代码调试，结果经人工核验。")
        self.assertNotIn("placeholder", {f["code"] for f in findings})

    def test_caption_does_not_require_a_colon(self):
        module = load("audit_text")
        findings = module.audit_text("根据结果作图，如图3所示。\n图3 温度随时间的变化")
        self.assertNotIn("unresolved-figure-table-reference", {f["code"] for f in findings})

    def test_figure_and_table_numbers_are_separate(self):
        module = load("audit_text")
        findings = module.audit_text("结果见图2和表2。\n图2 温度变化")
        self.assertTrue(any("表2" in f["message"] for f in findings))

    def test_keyword_separator_not_assumed(self):
        module = load("audit_final_surface")
        findings = module.audit("关键词：有限体积法；热湿耦合")
        self.assertNotIn("keyword-separator", {f["code"] for f in findings})

    def test_wrapped_abstract_is_checked_as_a_paragraph(self):
        module = load("audit_text")
        text = "摘要\n针对问题一，采用有限体积法建立传递模型，\n求解得中心温度为33.5753℃。\n关键词：热湿传递\n问题一1800s结果见下文。"
        codes = {f["code"] for f in module.audit_text(text)}
        self.assertNotIn("abstract-result-missing", codes)
        self.assertNotIn("abstract-question-missing", codes)

    def test_caption_title_can_start_with_a_number(self):
        module = load("audit_text")
        findings = module.audit_text("结果见表2。\n表2 30分钟内药材的温度")
        self.assertNotIn("unresolved-figure-table-reference", {f["code"] for f in findings})


class PackageAuditTests(unittest.TestCase):
    def make_package(self, members):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "support.zip"
        with ZipFile(path, "w") as archive:
            for name, content in members:
                archive.writestr(name, content)
        return path

    def codes(self, path, **kwargs):
        report = load("audit_support_package").audit_package(path, **kwargs)
        return {f["code"] for f in report["findings"]}

    def test_valid_unicode_folder_and_source(self):
        path = self.make_package([("支撑材料/q1_solve.py", "value = 1\n"), ("支撑材料/result1.xlsx", b"example")])
        report = load("audit_support_package").audit_package(path, required=["result1.xlsx"], compile_python=True)
        self.assertFalse(any(f["severity"] == "high" for f in report["findings"]))

    def test_dangling_path_operator_is_detected(self):
        path = self.make_package([("q2_solve.py", "from pathlib import Path\nOUT = Path(__file__).parent /\n")])
        self.assertIn("python-syntax", self.codes(path, compile_python=True))

    def test_question_mark_archive_shell_is_detected(self):
        self.assertIn("invalid-member-name", self.codes(self.make_package([("??????/result1.xlsx", b"data")])))

    def test_json_escaped_personal_path_is_detected(self):
        import json
        path = self.make_package([("audit.json", json.dumps({"result": r"C:\Users\person\Desktop\result1.xlsx"}))])
        self.assertIn("personal-path", self.codes(path))

    def test_mocked_summary_is_detected(self):
        import json
        data = {"temperature": [[0, 0]], "moisture": [[0, 0]], "minimum_properties": [1, 1], "maximum_properties": [1, 1]}
        path = self.make_package([("q2_summary.json", json.dumps(data))])
        self.assertIn("mock-summary", self.codes(path))

    def test_missing_required_result(self):
        self.assertIn("required-missing", self.codes(self.make_package([("q1_solve.py", "x = 1")]), required=["result1.xlsx"]))

    def test_unsafe_member_is_detected_without_extracting(self):
        self.assertIn("unsafe-member-path", self.codes(self.make_package([("../outside.txt", "data")])))

    def test_compile_does_not_execute_source(self):
        path = self.make_package([("q1_solve.py", "raise RuntimeError('must not execute')\n")])
        self.assertNotIn("python-syntax", self.codes(path, compile_python=True))


if __name__ == "__main__":
    unittest.main()
