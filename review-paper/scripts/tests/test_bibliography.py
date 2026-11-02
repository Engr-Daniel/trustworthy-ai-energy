"""Bibliography rendering must preserve math and escape ordinary text."""
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from make_bib import latex
class BibliographyTests(unittest.TestCase):
    def test_superscript_math_keeps_delimiters(self):
        self.assertEqual(latex("FMS$^2$: feature matching"), "FMS$^2$: feature matching")
    def test_literal_special_characters_are_escaped(self):
        self.assertEqual(latex("A & B_1: 20%"), r"A \& B\_1: 20\%")
    def test_unicode_hyphen_uses_tex_safe_form(self):
        self.assertEqual(latex("domain\u2010shift"), "domain-shift")
if __name__ == "__main__": unittest.main()
