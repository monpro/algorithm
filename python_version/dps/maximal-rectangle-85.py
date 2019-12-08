class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix[0])
        heights = [0 for _ in range(n)]
        result = 0
        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            result = max(result, self.largestRectangleArea(heights))
        return result

    def largestRectangleArea(self, heights):
        stack = [-1]
        heights.append(0)
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        
        heights.pop()
        return result

if __name__ == "__main__":
    l = Solution()
    test = [["1"]]
    print(l.maximalRectangle(test))