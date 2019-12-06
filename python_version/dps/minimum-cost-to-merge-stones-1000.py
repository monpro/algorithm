class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if n <= 1:
          return False

        prefix = [0] * (n + 1)
        memo = [[[0 for _ in range(K + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n):
          prefix[i + 1] = prefix[i] + stones[i]
        def helper(i, j, targetPiles):
          if memo[i][j][targetPiles] != 0:
            return memo[i][j][targetPiles]
          
          if targetPiles == 1:
            subMinCost = helper(i, j, K)
            if subMinCost != float('Inf'):
              memo[i][j][targetPiles] = prefix[j] - prefix[i - 1] + subMinCost
            else:
              memo[i][j][targetPiles] = subMinCost
            return memo[i][j][targetPiles]
          
          minCost = float('Inf')

          for k in range(i, j):
            leftCost = helper(i, k, targetPiles - 1)
            if leftCost == float("Inf"):
              continue
            rightCost = helper(k + 1, j, 1)
            if rightCost == float("Inf"):
              continue
            minCost = min(leftCost + rightCost, minCost)
          memo[i][j][targetPiles] = minCost
          print(memo)
          return minCost

        result = helper(1, n, 1)
        if result == float("Inf"):
          return -1
        else:
          return result
       
          
      
if __name__ == "__main__":
    l = Solution()
    stones = [3,2,4,1]
    K = 2
    print(l.mergeStones(stones, K))