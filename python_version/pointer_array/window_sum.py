class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if nums == [] or nums is None or k == 0 or len(nums) < k:
            return []
        result, sum_p = [], 0
        for i in range(k):
            sum_p += nums[i]
        result.append(sum_p)
        move_space = len(nums) - k + 1
        i, left, right = 1, 0, k

        while i < move_space:
            left_value = nums[left]
            right_value = nums[right]
            sum_p -= left_value
            sum_p += right_value

            result.append(sum_p)

            left += 1
            right += 1
            i += 1
        return result
