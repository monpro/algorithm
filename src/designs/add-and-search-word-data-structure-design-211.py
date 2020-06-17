import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        self.result = False
        self.dfs(node, word)
        return self.result
    
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.result = True
            return
        if word[0] == '.':
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            child = node.children.get(word[0])
            if not child:
                return
            self.dfs(child, word[1:])
        
        