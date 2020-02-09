class Solution:
    result = 0
    def maxLength(self, arr: List[str]) -> int:
        self.helper([], 0, arr)
        return self.result
    
    def helper(self, temp, start, arr):
        self.result = max(self.result, len("".join(temp)))
        for i in range(start, len(arr)):
            temp.append(arr[i])
            tempStr = "".join(temp)
            if len(set(tempStr)) == len(tempStr):
                self.helper(temp, i + 1, arr)
            temp.pop()