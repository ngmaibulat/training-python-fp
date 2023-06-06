import unittest

from src.b_map import capitalize_names


class TestCapitalizeNames(unittest.TestCase):
    def test_capitalize_names_empty_list(self):
        names = []
        expected = []
        result = capitalize_names(names)
        self.assertEqual(result, expected)

    def test_capitalize_names_all_lowercase(self):
        names = ["alice", "bob", "charlie"]
        expected = ["Alice", "Bob", "Charlie"]
        result = capitalize_names(names)
        self.assertEqual(result, expected)

    def test_capitalize_names_mixed_case(self):
        names = ["AlIce", "bOB", "cHARLIE"]
        expected = ["Alice", "Bob", "Charlie"]
        result = capitalize_names(names)
        self.assertEqual(result, expected)

    def test_capitalize_names_all_uppercase(self):
        names = ["ALICE", "BOB", "CHARLIE"]
        expected = ["Alice", "Bob", "Charlie"]
        result = capitalize_names(names)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
