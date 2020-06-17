import collections
class Solution:
    def groupThePeople(self, groupSizes):
        group = collections.defaultdict(list)
        n = len(groupSizes)
        for i in range(n):
            group[groupSizes[i]].append(i)
        result = []
        for key in group:
            indexes = group[key]
            for i in range(0, len(indexes), key):
                result.append(indexes[i:i+key])
        # for i, (size, indexes) in enumerate(group.items()):
        #     if len(indexes) == size:
        #         result.append(indexes)
        #     else:
        #         while len(indexes) > 0:
        #             temp = []
        #             for i in range(size):
        #                 temp.append(indexes.pop(0))
        #             result.append(temp)
        return result


if __name__ == "__main__":
    l = Solution()
    test = [2,1,3,3,3,2]
    l.groupThePeople(test)    