class WordDictionary:
    """
Problem: Design Add and Search Words Data Structure
Difficulty: Medium
LeetCode: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Pattern: Trie + DFS Backtracking
Topics: Trie, Recursion, Backtracking, HashMap
Time Complexity:
    addWord -> O(L)
    search -> O(26^k) worst case (k = '.' positions)
Space Complexity: O(N * L)
Key Insight: '.' triggers DFS over all children nodes in Trie
"""
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def backtracking(i, node):
            if i == len(word):
                return node.is_end_of_word

            ch = word[i]

            if ch != '.':
                if ch not in node.children:
                    return False
                return backtracking(i + 1, node.children[ch])

            for child in node.children.values():
                if backtracking(i + 1, child):
                    return True

            return False

        return backtracking(0, self.root)