from strings.implement_trie import Trie

class TestTrie:

    def test_basic_operations(self):
        trie = Trie()

        trie.insert("apple")

        assert trie.search("apple") is True
        assert trie.search("app") is False
        assert trie.startsWith("app") is True

        trie.insert("app")
        assert trie.search("app") is True

    def test_prefix_only(self):
        trie = Trie()

        trie.insert("car")
        assert trie.startsWith("ca") is True
        assert trie.startsWith("cat") is False

    def test_empty_trie(self):
        trie = Trie()

        assert trie.search("a") is False
        assert trie.startsWith("a") is False