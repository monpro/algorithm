class Solution:
    def groupAnagrams(self, strs):
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        result = []
        map = dict()
        for string in strs:
            key = 1
            for s in string:
                key *= prime[ord(s) - ord('a')]
            if key not in map:
                map[key] = [string]
            else:
                map[key].append(string)
        for key in map:
            result.append(map[key])
        return result