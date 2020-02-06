class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = [n for _ in range(n)]
        not_swap = [n for _ in range(n)]
        swap[0], not_swap[0] = 1, 0
        for i in range(1, n):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap[i] = min(swap[i - 1] + 1, swap[i])
                not_swap[i] = not_swap[i - 1]
            
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                not_swap[i] = min(swap[i - 1], not_swap[i])
                swap[i] = min(not_swap[i - 1] + 1, swap[i])
                
        return min(swap[-1], not_swap[-1])