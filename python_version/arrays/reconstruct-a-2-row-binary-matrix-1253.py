class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        upperList = [0 for _ in range(n)]
        lowerList = [0 for _ in range(n)]
        
        for i, v in enumerate(colsum):
            if v == 1:
                if upper > lower:
                    upper -= 1
                    upperList[i] = 1
                else:
                    lower -= 1
                    lowerList[i] = 1
            
            elif v == 2:
                upper -= 1
                lower -= 1
                upperList[i] = 1
                lowerList[i] = 1
        return [upperList, lowerList] if upper == 0 and lower == 0 else []