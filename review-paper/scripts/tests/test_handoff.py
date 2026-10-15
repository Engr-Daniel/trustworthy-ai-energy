"""Check workbook comparison boundaries and abstract container extraction."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "review-paper/scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module

class HandoffTests(unittest.TestCase):
    def test_archived_workbook_mapped_values_match(self):
        module = load("audit_workbook")
        report = module.audit(ROOT / "review-paper/corpus/Industrial_Inspection_Corpus_Tracker.xlsx")
        for tab, result in report.items():
            self.assertEqual(result["cell_difference_count"], 0, tab)
            self.assertEqual(result["csv_only_keys"], [], tab)
            self.assertEqual(result["xlsx_only_keys"], [], tab)
        self.assertEqual(report["Searches"]["xlsx_rows"], 19)
        self.assertEqual(report["Identification"]["source_fields_absent_from_workbook"], ["Identity"])
        self.assertEqual(report["Searches"]["representation_difference_count"], 19)

    def test_abstract_container_excludes_following_page_text(self):
        module = load("retrieve_pilot_abstracts")
        parser = module.AbstractParser()
        parser.feed('<meta name="description" content="generic teaser"><div id="abstract"><h2>Abstract</h2><p>Evidence <em>text</em>.</p></div><p>References excluded.</p>')
        self.assertEqual(module.text(parser.abstract()), "Abstract Evidence text .")
        self.assertNotIn("References", parser.abstract())

    def test_ieee_embedded_abstract_is_recovered_without_running_scripts(self):
        module = load("retrieve_pilot_abstracts")
        page = '<script>xplGlobal.document.metadata={"title":"Synthetic fixture","abstract":"Actual <b>abstract</b> text","sections":{"abstract":"true"}};</script>'
        self.assertEqual(module.extract_html_abstract(page), "Actual abstract text")

    def test_malformed_or_unrelated_metadata_does_not_become_abstract(self):
        module = load("retrieve_pilot_abstracts")
        self.assertEqual(module.extract_html_abstract('<script>xplGlobal.document.metadata={broken;</script>'), "")
        self.assertEqual(module.extract_html_abstract('<script>other.metadata={"abstract":"Unrelated"};</script>'), "")

    def test_generic_page_description_is_not_an_abstract(self):
        module = load("retrieve_pilot_abstracts")
        parser = module.AbstractParser()
        parser.feed('<meta name="description" content="publisher homepage">')
        self.assertEqual(parser.abstract(), "")

if __name__ == "__main__":
    unittest.main()
