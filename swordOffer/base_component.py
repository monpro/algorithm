class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 1:
            return 1
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent < 0 :
            return float(1)/ self.helper(1,base,-exponent)
        else:
            return self.helper(1,base,exponent)

    def helper(self,result,base,exponent):
        if exponent == 0:
            return result
        else:
            return self.helper(result * base, base, exponent - 1)



