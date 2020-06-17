import itertools
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for p in itertools.permutations(sorted(A, reverse=True)):
            if p[0] * 10 + p[1] < 24 and p[2] < 6:
                return f'{p[0]}{p[1]}:{p[2]}{p[3]}'
        
        return ""
        
    