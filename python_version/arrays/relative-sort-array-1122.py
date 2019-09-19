class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if not arr1 or not arr2:
          return arr1
        result = []
        arr_map = dict()
        for i in arr2:
          arr_map[i] = arr1.count(i)
        for key in arr2:
          for i in range(arr_map[key]):
            result.append(key)
            arr1.remove(key)
            # print(arr_map[key])
        # for i in arr1:
        #   if i not in arr2:
        arr1 = sorted(arr1)
        for i in arr1:
          result.append(i)
        return result

if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    l = Solution()
    l.relativeSortArray(arr1, arr2)
