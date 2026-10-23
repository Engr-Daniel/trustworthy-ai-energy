"""Version linkage: link only on author evidence, never on title alone; digests stay page-located."""
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from verify_version_linkage import classify
from fulltext_digest import digest

def rec(pid, authors, title="Anomaly Detection under Shift", rtype="article", year="2025", venue="Journal A", doi="", arxiv=""):
    return {"Paper ID": pid, "Full Title": title, "Full Authors": authors, "Record Type": rtype, "Year": year,
            "Venue / Journal": venue, "DOI": doi, "arXiv ID": arxiv}

class LinkageTests(unittest.TestCase):
    def test_name_order_does_not_block_a_link(self):
        a = rec("O1", "Gibbons Tom; Pierce Gareth", rtype="book-chapter")
        b = rec("O2", "Thomas Gibbons; Gareth Pierce", rtype="conference-paper")
        self.assertEqual(classify(a, b)[0], "Linked - same study")

    def test_same_title_different_authors_is_not_linked(self):
        self.assertEqual(classify(rec("O1", "Wen Chang"), rec("O2", "Debabrata Mukherjee; Vasilis Sarhosis"))[0],
                         "Not linked - distinct works")

    def test_single_shared_non_first_author_stays_unverified(self):
        a, b = rec("O1", "Chih-Min Lo"), rec("O2", "Ying-Jui Huang; Fu Li Hsiao; Hsing-Wen Wang; Chih-Min Lo", rtype="preprint")
        self.assertEqual(classify(a, b)[0], "Unverified - partial author overlap")

    def test_missing_authors_link_only_for_identifier_free_seed(self):
        seed, found = rec("P05", ""), rec("O3", "Amine Heddoub; Ali Siadat", doi="10.1/x")
        self.assertEqual(classify(found, seed)[0], "Linked - same study")
        self.assertEqual(classify(found, rec("C0048", "", doi="10.1/y"))[0], "Unverified - insufficient metadata")

    def test_non_latin_titles_are_spurious_candidates(self):
        a, b = rec("O1", "A B", title="НЕЙРОСЕТЕВОЙ АНАЛИЗ"), rec("O2", "C D", title="滚动轴承智能故障诊断")
        self.assertEqual(classify(a, b)[0], "Not linked - spurious candidate")

    def test_digest_snippets_carry_page_numbers(self):
        text = "\n[[page 1]]\nAbstract. Industrial inspection of insulators.\n[[page 2]]\nWe evaluate under domain shift.\n"
        d = digest("O9", text, 3, 40)
        self.assertIn("p2: ...", d)
        self.assertIn("R3 shift/OOD/robustness (hits=1)", d)

if __name__ == "__main__":
    unittest.main()
