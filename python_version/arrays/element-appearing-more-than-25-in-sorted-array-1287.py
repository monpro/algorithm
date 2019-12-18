class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        interval = len(arr) / 4
        
        for i in range(n - interval):
            if arr[i] == arr[i + interval]:
                return arr[i]
        return -1
        