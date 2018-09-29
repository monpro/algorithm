class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits) == 0:
            return result
        map = {'2':'abc','3':'edf','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'};
        self.helper(result, "", digits,map);
        return result

    def helper(self,result,string, digits, map):
        if len(string) == len(digits):
            result.append(string)
            return

        for i in map[digits[len(string)]]:
            string += i
            self.helper(result,string,digits,map)
            string = string[:-1]


l = Solution()
print(l.letterCombinations('234'))