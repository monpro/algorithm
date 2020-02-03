class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left, right = 0, n - 1
        
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp == target:
                return [left + 1, right + 1]
            elif temp > target:
                right -= 1
            else:
                left += 1
            
            
    def twoSumWithBinarySearch(self, numbers, target):
      n = len(numbers)
      for i in range(n - 1):
        left, right = i + 1, n - 1
        toFindVal = target - numbers[i]
        while left <= right:
          mid = left + (right - left) // 2
          if numbers[mid] == toFindVal:
            return [i + 1, mid + 1]
          elif numbers[mid] > toFindVal:
            right = mid - 1
          else:
            left = mid + 1