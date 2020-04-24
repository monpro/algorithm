<<<<<<< HEAD
=======
import collections

>>>>>>> 664fe46... use slide window to handle the concentation
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
<<<<<<< HEAD
        length = len(words[0])
        wordMap = dict()
        wordList = [s[(i - 1) * length: i * length] for i in range(1, len(s) // length)]
        result = []
        length = len(words)
        for i in wordList:
            wordMap[i] = 0
        for i in words:
            if i not in wordMap:
                return []
            else:
                wordMap[i] += 1
        
        start, end, count = 0, 0, len(words)
        while start < len(wordList) and end < len(wordList):

            if wordMap[wordList[end]] > 0:
                count -= 1
                wordMap[wordList[end]] -= 1
                end += 1
                print(count, wordMap, end)
            elif wordMap[wordList[end]] == 0:
                start = end
                end = end
                count = len(words)
                for i in words:
                    wordMap[i] += 1
            while count == 0:
                result.append(start)
                start += 1 
                end = start
                count = len(words)
                for i in words:
                    wordMap[i] += 1
                


        result = [len(words[0]) * i for i in result]
        return result

            

if __name__ == "__main__":
    l = Solution()
    s = "barfoofoobarthefoobarman"

    words = ["bar","foo","the"]
    print(l.findSubstring(s, words))


  
        
=======
        if not words:
          return []
        k = len(words[0])
        result = []
        for left in range(k):
          d = collections.Counter(words)
          for right in range(left + k, len(s) + 1, k):
            word = s[right - k: right]
            d[word] -= 1
            while d[word] < 0:
              d[s[left: left + k]] += 1
              left += k
            if left + k * len(words) == right:
              result.append(left)
        return result
            
>>>>>>> 664fe46... use slide window to handle the concentation
