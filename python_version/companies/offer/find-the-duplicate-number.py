class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start , end = 1, len(nums) - 1
        while end >= start:
            middle = start + (end - start) // 2
            count = self.countRange(nums, start, middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count > middle - start + 1:
                end = middle
            else:
                start = middle + 1
        return -1

    def countRange(self,numbers,start, end):
        count = 0
        for i in range(len(numbers)):
            if start <= numbers[i] <= end:
                count += 1
        return count

