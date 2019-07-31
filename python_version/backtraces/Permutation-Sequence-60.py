class Solution:
    def getPermutation(self, n, k):
        result = ""
        num = []
        fact = 1
        for i in range(1, n + 1):
            fact *= i
            num.append(i)
        # fact is the fatorial from 1 ... n
        # index start from 0
        k -= 1
        for i in range(n):
            fact = fact // (n - i)

            index = k // fact
            result += str(num.pop(index))
            k -= index * fact
        return result


