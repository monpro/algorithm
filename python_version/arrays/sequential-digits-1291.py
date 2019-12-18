class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        for digit in range(1, 9):
          cur, nextDigit = digit, digit
          while cur <= high and nextDigit < 10:
            if cur >= low:
              result.append(cur)
            nextDigit += 1
            cur = cur * 10 + nextDigit
        return sorted(result)



if __name__ == "__main__":
    low = 1000
    high = 14000
    l = Solution()
    print(l.sequentialDigits(low, high))