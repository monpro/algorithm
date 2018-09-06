class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        self.result = []
        visited = [0 for i in range(len(ss))]
        self.helper(ss,'',visited)
        self.result = list(set(self.result))
        self.result.sort()
        return self.result


    def helper(self,ss,substring,visited):
        if len(substring) == len(ss):
            self.result.append(substring)
            return

        for i in range(len(ss)):
            if visited[i] == 1:
                continue
            else:
                visited[i] = 1
                self.helper(ss,substring + ss[i],visited)
                visited[i] = 0
    def adjust_word(self,word):
        for i in range(len(word) - 1):
            if word[i] > word[i + 1]:
                word[i], word[i + 1] = word[i + 1], word[i]
        return word







l = Solution()
print(l.Permutation("abc"))


