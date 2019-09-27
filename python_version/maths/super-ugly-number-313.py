class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nums = [float('Inf') for i in range(n)]
        indexArray = [0 for i in range(len(primes))]
        nums[0] = 1
        for i in range(1, n):
          for index in range(len(indexArray)):
            nums[i] = min(nums[indexArray[index]] * primes[index], nums[i])
          for index in range(len(indexArray)):
            if nums[indexArray[index]] * primes[index] == nums[i]:
              indexArray[index] += 1 
        return nums[-1]


if __name__ == "__main__":
  l = Solution()
  print(l.nthSuperUglyNumber(12, [2,7,13,19]))
