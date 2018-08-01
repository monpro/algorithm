class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    '''
    #two pointer
    def twoSum(self, numbers, target):
        # write your code here

        L = [i for i in numbers]
        result = []
        #two pointers
        left,right = 0, len(numbers) - 1
        left_point,right_point = 0, len(numbers) - 1
        numbers.sort()
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1

            elif numbers[left] + numbers[right] > target:
                right -= 1

            elif numbers[left] + numbers[right] == target:
                for i in range(len(L)):
                    if L[i] == numbers[left]:
                        result.append(i)
                        break

                for i in range(len(L) -1 ,-1,-1):
                    if L[i] == numbers[right]:
                        result.append(i)
                        break
                result.sort()
                return result

        return []
        '''

    # hashmap
    def twoSum(self, numbers, target):
        # value----> index
        hashmap = dict()
        result = []
        for i in range(len(numbers)):
            if target - numbers[i] in hashmap:
                result.append(hashmap[target - numbers[i]])
                result.append(i)
                result.sort()
                return result
            hashmap[numbers[i]] = i

        return []

