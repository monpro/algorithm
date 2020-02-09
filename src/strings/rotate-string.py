class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        # write your code here
        if str is None or len(str) == 0:
            return

        offset = offset % len(str)

        self.reverse(str, 0, len(str) - offset - 1)
        self.reverse(str, len(str) - offset, len(str) - 1)
        self.reverse(str, 0, len(str) - 1)

    def reverse(self, str, start, end):
        i, j = start, end
        while i <= j:
            temp = str[i]
            str[i] = str[j]
            str[j] = temp
            i += 1
            j -= 1
