class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        dp_set = []
        for i in range(len(triangle)):
            dp_set.append([])
            for j in range(len(triangle[i])):
                dp_set[i].append(0)
        dp_set[0][0] = triangle[0][0]
        # Init
        for i in range(1, len(triangle)):
            dp_set[i][0] = dp_set[i - 1][0] + triangle[i][0]
            dp_set[i][i] = dp_set[i - 1][i - 1] + triangle[i][i]

        for i in range(1, len(triangle)):
            for j in range(1, i):
                dp_set[i][j] = min(dp_set[i - 1][j - 1], dp_set[i - 1][j]) + triangle[i][j]

        return min(dp_set[len(triangle) - 1])