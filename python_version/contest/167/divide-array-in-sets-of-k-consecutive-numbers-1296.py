import collections
class Solution(object):
    def isPossibleDivide(self, nums, k):
        count = collections.Counter(nums)
        sortedNums = sorted(nums)
        for key in sortedNums:
            if count[key] > 0:
                minVal = count[key]
                for i in range(key, key + k):
                    if count[i] < minVal:
                        return False
                    count[i] -= minVal
        return True