from src.b_map import capitalize_names


def test_capitalize_names_empty_list():
    names = []
    expected = []
    result = capitalize_names(names)
    assert result == expected


def test_capitalize_names_all_lowercase():
    names = ["alice", "bob", "charlie"]
    expected = ["Alice", "Bob", "Charlie"]
    result = capitalize_names(names)
    assert result == expected


def test_capitalize_names_mixed_case():
    names = ["AlIce", "bOB", "cHARLIE"]
    expected = ["Alice", "Bob", "Charlie"]
    result = capitalize_names(names)
    assert result == expected


def test_capitalize_names_all_uppercase():
    names = ["ALICE", "BOB", "CHARLIE"]
    expected = ["Alice", "Bob", "Charlie"]
    result = capitalize_names(names)
    assert result == expected
