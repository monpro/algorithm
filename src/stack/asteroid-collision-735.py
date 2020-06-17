class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 0:
            return []
        
        stack = []
        
        for val in asteroids:
            while len(stack) > 0 and stack[-1] > 0 and val < 0:
                if abs(val) == stack[-1]:
                    stack.pop()
                    break
                elif abs(val) > stack[-1]:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(val)
        return stack
                
                