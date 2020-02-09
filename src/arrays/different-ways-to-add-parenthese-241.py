class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if len(input) == 0:
          return []
        result = []
        for i in range(len(input)):
          if input[i] == '-' or input[i] == '+' or input[i] == '*':
            left = input[0 : i]
            right = input[i + 1 : ]
            leftRes = self.diffWaysToCompute(left)
            rightRes = self.diffWaysToCompute(right)
            for left in leftRes:
              for right in rightRes:
                if input[i] == '-':
                  result.append(left - right)
                elif input[i] == '+':
                  result.append(left + right)
                else:
                  result.append(left * right)
        if len(result) == 0:
          result.append(int(input))
        return result