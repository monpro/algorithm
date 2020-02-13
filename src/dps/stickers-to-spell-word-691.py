import collections
class Solution:
    def minStickers(self, stickers, target):
        count, result, n = collections.Counter(target), [float('Inf')], len(target)

        def dfs(dic, used, i):
            if i == n:
                result[0] = min(result[0], used)
            elif dic[target[i]] >= count[target[i]]:
                dfs(dic, used, i + 1)
            elif used < result[0] - 1:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker:
                            dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker:
                            dic[s] -= 1
        
        dfs(collections.defaultdict(int), 0, 0)

        if result[0] != float("Inf"):
            return result[0]
        else:
            return -1

if __name__ == "__main__":
    l = Solution()
    stickers = ["with", "example", "science"]
    target = "thehat"
    print(l.minStickers(stickers, target))


        

        