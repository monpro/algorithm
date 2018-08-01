# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if len(array) <= 1:
            return array
        '''
        # solution 1 using extra space
        # time complexity: O(n) space complexity: o(n)
        new_array = []
        for i in array:
            if i % 2 == 1:
                new_array.append(i)
        for i in array:
            if i % 2 == 0:
                new_array.append(i)
        return new_array
        '''

        '''
        solution2 not using extra 
        
        '''
        for i in range(1, len(array)):
            if array[i] % 2 == 1:   
                for j in range(i,0,-1):
                    if array[j - 1] % 2 == 0:
                        array[j], array[j - 1] = array[j - 1], array[j]
        return array

if __name__ == "__main__":
    l = Solution()
    print(l.reOrderArray([1,3,2,8,9,10,12,16,3,4,5,5,7,9,8]))

