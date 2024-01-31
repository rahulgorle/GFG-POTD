class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Solution:
    def insert(self, root, key):
        for i in key:
            ind = ord(i) - ord('a')
            if not root.children[ind]:
                root.children[ind] = TrieNode()
            root = root.children[ind]
        root.isEndOfWord = True
   
    def search(self, root, key):
        for i in key:
            ind = ord(i) - ord('a')
            if not root.children[ind]:
                return False
            root = root.children[ind]
        return root.isEndOfWord
