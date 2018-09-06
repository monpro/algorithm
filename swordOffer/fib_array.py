# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        fib_array = self.get_fib(n)

        return fib_array[n]

    # write code here
    def get_fib(self, n):
        results = [0 for i in range(n + 1)]
        if n <= 0:
            return results
        if n == 1:
            results[1] = 1
            return results
        if n == 2:
            results[1] = 1
            results[2] = 1
            return results
        if n > 2:
            results[1] = 1
            results[2] = 1
            for i in range(3, n + 1):
                results[i] = results[i - 1] + results[i - 2]
            return results


l = Solution()
print(l.Fibonacci(10))
