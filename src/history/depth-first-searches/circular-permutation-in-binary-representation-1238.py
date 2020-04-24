class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def helper(i):
            if i == 1:
                return [0, 1]
            temp = helper(i - 1)
            power = 2 ** (i - 1)
            return temp + [power + t for t in temp[::-1]]
        
        arr = helper(n)
        index = arr.index(start)
        return arr[index:] + arr[:index]