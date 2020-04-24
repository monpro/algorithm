class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 10 ** 9 + 7
        dps = collections.defaultdict(int)
        
        def helper(i, j, N):
            if (i, j, N) in dps:
                return dps[(i, j, N)]
            
            if 0 <= i < m and 0 <= j < n:
                if N == 0:
                    dps[(i, j, N)] = 0
                    return 0
                else:
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        dps[(i, j, N)] += helper(x, y, N - 1)
                    
                    return dps[(i, j, N)]
            else:
                dps[(i, j, N)] = 1
                return 1
        
        return helper(i, j, N) % mod