class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        if len(nums) <= 1:
            return nums
        # step1: find the maximum number of array
        '''
        target = nums[-1]

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid

        if nums[end] > nums[start]:
            position = end
        else:
            position = start
        '''
        position = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                position = i
        if position:
            self.rotated(nums,0, position)
            self.rotated(nums,position +1, len(nums) - 1)
            self.rotated(nums,0, len(nums) - 1)

        return nums


    def rotated(self, array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1



if __name__ == "__main__":
    l = Solution()
    print(l.recoverRotatedSortedArray([1,2,3,4,5]))
    print(l.recoverRotatedSortedArray([]))
    print(l.recoverRotatedSortedArray([1]))
    print(l.recoverRotatedSortedArray([2,3,1]))


