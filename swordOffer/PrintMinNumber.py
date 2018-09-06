# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ""
        if len(numbers) == 1:
            return numbers[0]

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if self.helper(str(numbers[i]) + str(numbers[j]), str(numbers[j]) + str(numbers[i])):
                    numbers[j], numbers[i] = numbers[i],numbers[j]
        string = ""
        for i in numbers:
            string += str(i)
        return int(string)

    def helper(self,string1,string2):
        if string1 < string2:
            return 0
        else:
            return 1

l = Solution()
l.PrintMinNumber([3,32,321])