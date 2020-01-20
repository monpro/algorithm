class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dps = collections.defaultdict(int)
        
        for i in arr:
            dps[i] = max(dps[i], dps[i - difference] + 1)
        return max(dps.values())