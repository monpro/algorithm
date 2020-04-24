from copy import deepcopy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = collections.defaultdict(int)
        for ch in chars:
            count[ch] += 1
        
        result = 0
        
        for word in words:
            temp = deepcopy(count)
            for i in range(len(word)):
                ch = word[i]
                if ch not in temp:
                    break
                elif temp[ch] == 0:
                    break
                elif i == len(word) - 1 and temp[ch] > 0:
                    result += len(word)
                else:
                    temp[ch] -= 1
        
        return result