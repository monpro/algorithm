class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        # write your code here


        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    def quickSelect(self, A, start, end, k):
        if start == end:
            return A[start]

        left = start
        right = end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        if right >= k and start <= right:
            return self.quickSelect(A, start, right, k)
        elif left <= k and left <= end:
            return self.quickSelect(A, left, end, k)
        else:
            return A[k]

