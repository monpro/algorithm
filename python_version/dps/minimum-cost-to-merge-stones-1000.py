class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if n == 1:
          return 0

        prefix = [0] * (n + 1)
        memo = [[[0 for _ in range(K + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n):
          prefix[i + 1] = prefix[i] + stones[i]
        result = self.helper(1, n, 1, K, prefix, memo)
        if result == float("Inf"):
          return -1
        else:
          return result
    def helper(self,i, j, targetPiles, K, prefix, memo):
        if memo[i][j][targetPiles] != 0:
          return memo[i][j][targetPiles]
        if j - i  + 1 < targetPiles:
          return float("Inf")
        
        if i == j:
          if targetPiles == 1:
            return 0
          else:
            return float("Inf")
        if targetPiles == 1:
          subMinCost = self.helper(i, j, K, K, prefix, memo)
          if subMinCost != float('Inf'):
            memo[i][j][targetPiles] = prefix[j] - prefix[i - 1] + subMinCost
          else:
            memo[i][j][targetPiles] = subMinCost
          return memo[i][j][targetPiles]
        
        minCost = float('Inf')

        for k in range(i, j):
          leftCost = self.helper(i, k, targetPiles - 1, K, prefix, memo)
          if leftCost == float("Inf"):
            continue
          rightCost = self.helper(k + 1, j, 1, K, prefix, memo)
          if rightCost == float("Inf"):
            continue
          minCost = min(leftCost + rightCost, minCost)
        memo[i][j][targetPiles] = minCost
        return minCost
        
       
          
      
if __name__ == "__main__":
    l = Solution()
    stones = [3,2,4,1]
    K = 2
    print(l.mergeStones(stones, K))