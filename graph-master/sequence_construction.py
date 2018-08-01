class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        # this problem could translated into
        # only one toplogical sorting result
        # how to keep it?

        if seqs == [[]] and org == []:
            return True
        if seqs == [] or org == [] and seqs + org != []:
            return False

        node_set = set()
        for i in seqs:
            for j in i:
                node_set.add(j)

        indegree_hash_map = dict((i, 0) for i in node_set)
        neighbours = dict((i, []) for i in node_set)
        for i in range(len(seqs)):
            for j in range(len(seqs[i]) - 1):
                neighbours[seqs[i][j]].append(seqs[i][j + 1])
                indegree_hash_map[seqs[i][j + 1]] += 1

        queue, result = [], []

        for i in indegree_hash_map:
            if indegree_hash_map[i] == 0:
                queue.append(i)
        if len(queue) != 1:
            return False

        while queue != []:
            e = queue.pop(0)
            result.append(e)
            for i in neighbours[e]:
                indegree_hash_map[i] -= 1
                if indegree_hash_map[i] == 0:
                    queue.append(i)
            if len(queue) != 1 and len(queue) != 0:
                return False

        if result == org:
            return True
        else:
            return False

