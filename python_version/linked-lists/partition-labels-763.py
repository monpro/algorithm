class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        rightMostDict = {}
        for i in range(len(S)):
          rightMostDict[S[i]] = i
        result = []
        lastRightMost = 0
        rightMost = 0
        for i in range(len(S)):
          rightMost = max(rightMostDict[S[i]], rightMost)
          if i == rightMost:
            result.append(rightMost - lastRightMost + 1)
            lastRightMost = rightMost + 1
            rightMost = 0
        return result

if __name__ == "__main__":
    l = Solution()
    l.partitionLabels("ababcbacadefegdehijhklij")