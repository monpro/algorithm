class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # maxRightval: the right largest val for arr[i]
        maxRightVal = -1
        n = len(arr)
        for i in range(n - 1, -1, -1):
            val = arr[i]
            arr[i] = maxRightVal
            maxRightVal = max(maxRightVal, val)
        return arr
            