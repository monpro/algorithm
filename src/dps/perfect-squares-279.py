<<<<<<< HEAD
import math
class Solution:
    def numSquares(self, n):
        if n == 0:
            return 0
        
        dp = [float("Inf") for i  in range(n+ 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]
        

=======
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
          return 0
        dp = [i for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
          j = 0
          while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
        return dp[-1]
<<<<<<< HEAD
>>>>>>> 64589e8... add dp solution of perfect squares
=======
      
    def numSquaresBfs(self, n):
      if n == 0:
        return 0
      i = 1
      squareList = []
      while i * i <= n:
        squareList.append(i * i)
        i += 1
      result = 0
      toCheck = set(n)
      while toCheck:
        result += 1
        temp = set()
        for number in toCheck:
          for square in squareList:
            if number == square:
              return result
            elif number < square:
              break
            else:
              temp.add(number - square)
        toCheck = temp
      return result
>>>>>>> 7f2b56c... add bfs solution to find shortest path
