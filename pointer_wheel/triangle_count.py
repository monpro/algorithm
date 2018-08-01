class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        result = []
        S.sort()
        count = 0
        # if from smallest to biggest, then cannot determine which value to add
        for i in range(len(S) - 1, 1, -1):
            # S[i] is the largest edge
            left, right = 0, i - 1

            while left < right:
                if S[left] + S[right] > S[i]:
                    count += right - left
                    right -= 1

                else:
                    left += 1

        return count
