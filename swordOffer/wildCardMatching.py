class Solution:
    def isMatch(self, s, p):
        """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?

        """
        memory = {}
        return self.dfs(s,0,p,0,memory)

    def dfs(self,s,sIndex, p, pIndex, memory):
        if pIndex == len(p):
            return sIndex == len(s)
        if sIndex == len(s):
            return self.isAllStar(p,pIndex)
        if (sIndex, pIndex) in memory:
            return memory[(sIndex, pIndex)]
        match = False

        if p[pIndex] == '*':
            match = self.dfs(s, sIndex + 1, p, pIndex,memory) or self.dfs(s,sIndex, p, pIndex + 1, memory)
        else:
            match = (p[pIndex] == s[sIndex] or p[pIndex] == '?') and self.dfs(s, sIndex + 1, p, pIndex + 1, memory)

            memory[(sIndex, pIndex)] = match
            return match

    def isAllStar(self,p,index):
        newStr = p[index:]
        for c in newStr:
            if c!= '*':
                return False
        return True