class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(T))]
        for i in range(len(T)):    
            while len(stack) > 0 and T[stack[-1]] < T[i]:
                peek = stack.pop()
                result[peek] = i - peek

            stack.append(i)

        # for i in range(len(result)):
        #     if result[i] > 0:
        #         result[i] = result[i] - i
        
        return result