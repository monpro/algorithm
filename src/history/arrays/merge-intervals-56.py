class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
          return []
        result = []
        for i in sorted(intervals, key = lambda i: i[0]):
          if result and i[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], i[1])
          else:
            result.append(i)
        return result


if __name__ == "__main__":
    l = Solution()
    print(l.merge([[1,4],[3,4],[7,8],[5,7]]))