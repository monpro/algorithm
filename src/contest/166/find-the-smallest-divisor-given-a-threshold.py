class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            sumVal = sum([(num + mid - 1)  // mid for num in nums])
            if sumVal > threshold:
                left = mid + 1
            else:
                right = mid
                
        return left