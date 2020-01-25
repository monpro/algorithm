import collections

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordCollections = collections.defaultdict(set)

        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.wordCollections[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        wordSet = self.wordCollections[len(word)]
        if word in wordSet:
            return True
        if not wordSet:
            return False
        for i, char in enumerate(word):
            if char == '.':
                continue
            tempSet = set()
            for w in wordSet:
                if w[i] == word[i]:
                    tempSet.add(w)
            if not tempSet:
                return False
            wordSet = tempSet
        return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)