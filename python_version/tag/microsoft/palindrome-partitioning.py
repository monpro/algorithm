class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        subset,result = [],[]
        if len(s) == 0:
            return result
        self.helper(subset,result,s,0)
        return result
    def helper(self,subset,result,s,position):
        if position == len(s):
            result.append([i for i in subset])
            return
        for i in range(position,len(s)):
            subString = s[position:i+1]
            if self.is_palin(subString):
                subset.append(subString)
                self.helper([i for i in subset],result,s,i + 1)
                subset.pop(-1)
    def is_palin(self,substring):
        left,right = 0, len(substring - 1)
        while left < right:
            if substring[left] == substring[right]:
                left += 1
                right -= 1
            else:
                return False
        return True



