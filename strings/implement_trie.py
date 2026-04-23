class Node:
    def __init__(self, isendofword = False):
        self.isendofword = isendofword
        self.children = {}

class Trie:
    """
Problem: Implement Trie (Prefix Tree)
Difficulty: Medium
Pattern: Trie / Prefix Tree / String Data Structure
LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/
"""
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        currnode = self.root
        for ch in word:
            if ch not in currnode.children:
                newNode = Node()
                currnode.children[ch] = newNode
            currnode = currnode.children[ch]
        currnode.isendofword = True


    def search(self, word: str) -> bool:
        currnode = self.root
        for ch in word:
            if ch not in currnode.children:
                return False
            currnode = currnode.children[ch]
            
        return currnode.isendofword

    def startsWith(self, prefix: str) -> bool:
        currnode = self.root
        for ch in prefix:
            if ch not in currnode.children:
                return False
            currnode = currnode.children[ch]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)