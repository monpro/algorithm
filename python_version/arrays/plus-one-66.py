class Solution(object):
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
