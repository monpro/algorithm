class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n > 10:
            n = 10
        result = 10
        
        baseInteger = 9
        restInteger = 9
        while n > 1 and restInteger > 0:
            result += baseInteger * restInteger
            baseInteger = baseInteger * restInteger
            restInteger -= 1
            n -= 1
        return result