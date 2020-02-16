class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s, stack):
            for i in s:
                if i != '#':
                    stack.append(i)
                elif i == '#' and stack:
                    stack.pop()
            return stack
        
        return helper(S, []) == helper(T, [])
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        backS, backT = 0, 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not(i >= 0 and j>= 0 and S[i] == T[j]):
                return i == j == - 1
            i -= 1
            j -= 1
