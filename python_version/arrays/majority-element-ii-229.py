class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
          return []
        candidate_a, candidate_b, count_a, count_b = 0, 1, 0, 0
        for num in nums:
          if num == candidate_a:
            count_a += 1
          elif num == candidate_b:
            count_b += 1
          elif count_a == 0:
            candidate_a, count_a = num, 1
          elif count_b == 0:
            candidate_b, count_b = num, 1
          else:
            count_a -= 1
            count_b -= 1
        return [i for i in [candidate_a, candidate_b] if nums.count(i) > len(nums) // 3]
