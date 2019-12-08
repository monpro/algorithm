class Solution:
    def largestRectangleArea(self, heights):
      n = len(heights)
      left = [1 for i in range(n)]
      right = [1 for i in range(n)]
      result = 0

      for i in range(n):
        j = i - 1
        while j >= 0:
          if heights[j] >= heights[i]:
            left[i] += left[j]
            j -= left[j]
          else:
            break
      for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n:
          if heights[j] >= heights[i]:
            right[i] += right[j]
            j += right[j]
          else:
            break
      for i in range(n):
        result = max(result, (right[i] + left[i] - 1) * heights[i] )
      return result
    
    def largestRectangleAreaStack(self, heights):
      ans = 0
      stack = [-1]
      heights.append(0)
      for i in range(heights):
        while heights[i] < heights[stack[-1]]:
          h = heights[stack.pop()]
          w = i - stack[-1] - 1
          ans = max(ans, h * w)
        stack.append(i)
      heights.pop()
      return ans        