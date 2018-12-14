class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if prerequisites == []:
            return True

        # create indegree hashmap and all nodes
        node_set = set()
        for i in prerequisites:
            for j in i:
                node_set.add(j)
        indegree_hash_map = dict((i, 0) for i in node_set)
        neighbours = dict((i, []) for i in node_set)
        print(prerequisites)
        for i in prerequisites:
            indegree_hash_map[i[1]] += 1
            neighbours[i[0]].append(i[1])
        queue, result = [], []
        for i in indegree_hash_map:
            if indegree_hash_map[i] == 0:
                queue.append(i)

        while queue != []:
            e = queue.pop(0)
            result.append(e)
            for i in neighbours[e]:
                indegree_hash_map[i] -= 1

                if indegree_hash_map[i] == 0:
                    queue.append(i)

        print(result)
        return len(result) == len(node_set)
