class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
#     def restoreIpAddresses(self, s):
#         # write your code here
#         if len(s) < 4 or len(s) > 12:
#             return []
#         result = []
#         self.helper(s, result, [0], 0)
#         return result
#
#     def helper(self, s, result, dots, index):
#         if index == len(s) and self.isValidString(s[dots[-1]: index]):
#             result.append(self.getIpString(s, dots))
#             return
#         for i in range(1,len(s) + 1):
#             if self.isValidString(s[dots[-1]: i]):
#                 dots.append(i)
#                 print(dots)
#                 self.helper(s, result, dots, i)
#                 dots.pop()
#
#
#     def isValidString(self, s):
#         print(s)
#         if "0" <= s <= "255":
#             print(s)
#             return True
#         else:
#             return False
#
#     def getIpString(self, s, dots):
#         ipString = "";
#         index = 0
#         for i in range(len(s)):
#             if i == int(dots[index]):
#                 ipString += "."
#                 index += 1
#             ipString += s[i]
#         return ipString
#
# l = Solution()
# print(l.restoreIpAddresses("25525511135"))