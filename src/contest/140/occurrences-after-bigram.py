class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textArray = text.split(' ')
        if len(textArray) < 3:
            return []
        result = []
        for i in range(len(textArray) - 2):
            if textArray[i] == first and textArray[i + 1] == second:
                result.append(textArray[i + 2])
        
        return result