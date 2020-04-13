class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
        
        low = 0
        high = min(m, n)
        while low <= high:
            mid = low + (high - low) // 2
            if self.inBound(prefix, threshold, mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high
    
    def inBound(self, prefix, threshold, mid):
        for i in range(mid, len(prefix)):
            for j in range(mid, len(prefix[0])):
                if prefix[i][j] - prefix[i - mid][j] - prefix[i][j - mid] + prefix[i - mid][j - mid] <= threshold:
                    return True
        return False