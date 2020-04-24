class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            if height[left] < height[right]:
                temp = width * height[left]
                left += 1
            else:
                temp = width * height[right]
                right -= 1
            if temp > result:
                result = temp
        return result
            
        