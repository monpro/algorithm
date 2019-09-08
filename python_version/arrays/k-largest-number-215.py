import queue


class Solution(object):

  def findKthLargest(self, nums, k):
    return self.quickSelect(nums, 0, len(nums) - 1, k)

  def quickSelect(self, nums, low, high, k):
    pivot = low

    for j in range(low, high):
      if nums[j] <= nums[high]:
        nums[pivot], nums[j] = nums[j], nums[pivot]
        pivot += 1
    # all index < pivot ==> nums[index] <= nums[high]
    nums[pivot], nums[high] = nums[high], nums[pivot]
    # all index <= pivot ==> nums[index] <= nums[high]
    # count means the number of elements >= nums[high]
    count = high - pivot + 1
    if count == k:
      return nums[pivot]
    if count > k:
      return self.quickSelect(nums, pivot + 1, high, k)
    if count < k:
      return self.quickSelect(nums, low, pivot - 1, k - count)

  def findKthLargestWithQueue(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    prQueue = queue.PriorityQueue()
    for num in nums:
      prQueue.put(num)

      if prQueue.qsize() > k:
        prQueue.get()
    return prQueue.get()


if __name__ == "__main__":
  l = Solution()
  print(l.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
