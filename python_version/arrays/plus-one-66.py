class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        ugly solution
        """
        digit = ""
        for e in digits:
            digit += str(e)
        digit = int(digit)
        digit += 1
        digit = str(digit)
        result = []
        for i in digit:
            result.append(i)
        return result

    def plusOne(self, digits):
        '''
        nice solution
        :param digits:
        :return:
        '''
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        newNumbers = [1] + digits
        return newNumbers



if __name__ == "__main__":
    l = Solution()
    l.plusOne([1,2,3,4,5])