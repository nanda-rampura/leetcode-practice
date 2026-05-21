from trie.word_dictionary import WordDictionary

def test_basic_add_and_search():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    assert wd.search("bad") is True
    assert wd.search("dad") is True
    assert wd.search("mad") is True
    assert wd.search("pad") is False


def test_wildcard_search():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    assert wd.search("..d") is True
    assert wd.search("...") is True


def test_edge_cases():
    wd = WordDictionary()
    wd.addWord("a")

    assert wd.search("a") is True
    assert wd.search(".") is True
    assert wd.search("b") is False