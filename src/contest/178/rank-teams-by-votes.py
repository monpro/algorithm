class Solution:
    # def rankTeams(self, votes):
    #     count = [{} for _ in range(len(votes))]

    #     for i in range(len(votes)):
    #         for j in range(len(votes[i])):
    #             char = votes[i][j]
    #             if char not in count[j]:
    #                 count[j][char] = 1
    #             else:
    #                 count[j][char] += 1

    def rankTeams(self, votes):
        import collections
        # for each new letter create an array of 26 0s
        count = collections.defaultdict(lambda: [0] * 26)

        for vote in votes:
            for rank, c in enumerate(vote):
                count[c][rank] -= 1
        print(count)
        # sort by 1) rank (item[1]); 2) by alphabet (item[0])}
        count = sorted(count.items(), key=lambda item: (item[1], item[0]))

        return ''.join(item[0] for item in count)

if __name__ == "__main__":
    Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"])     
    print(sorted([5,2,1,4]))
        
        
            