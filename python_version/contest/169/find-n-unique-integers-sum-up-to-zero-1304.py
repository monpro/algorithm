class Solution:
    def sumZero(self, n: int) -> List[int]:
        # n = 0, []
        # n = 1, [0]
        # n = 2, [-1,1]
        # n = 3, [-2, 0, 2]
        # n = 4, [-3, -1, 1, 3]
        # n = 5 ,[-4, -2, 0, 2, 4]
        
        # result = [0 for _ in range(n)]
        # for i in range(n):
        #     result[i] = i * 2 - n + 1
        # return result
        result = []
        if n % 2 != 0:
            result.append(0)
        
        for i in range(n // 2):
            result.append(i + 1)
            result.append(-i - 1)
        return result
            
        