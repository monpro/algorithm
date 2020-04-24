class Solution:
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = [i for i in range(1, 10)]
        
        while len(queue) > 0:
            num = queue.pop(0)
            if num >= low and num <= high:
                result.append(num)
            lastDigit = num % 10
            cur = num * 10 + lastDigit + 1
            if lastDigit < 9 and cur <= high:
                queue.append(cur)
        return result

#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         result = []
        
#         for i in range(1, 9):
#             num = base = i
            
#             while num <= high and base < 10:
#                 if num >= low:
#                     result.append(num)
                
#                 base += 1
#                 num = num * 10 + base
        
#         return sorted(result)