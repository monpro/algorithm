class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """

    def countAndSay(self, n):
        result = "1"
        for i in range(n - 1):
            nextResult = ""
            count = 1
            for j in range(len(result)):
                if j == len(result) - 1 or result[j] != result[j + 1]:
                    nextResult += str(count) + result[j]
                    count = 1
                else:
                    count += 1
            result = nextResult

        return result