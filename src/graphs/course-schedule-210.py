class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        result = []
        if not prerequisites:
            for i in range(numCourses):
                result.append(i)
            return result
        # create indegree_hash_map and node_set
        node_set = set()
        queue = []
        for i in prerequisites:
            for j in i:
                node_set.add(j)
        indegree_hash_map = dict((i, 0) for i in node_set)
        neighbours = dict((i, []) for i in node_set)
        for i in prerequisites:
            neighbours[i[1]].append(i[0])
            indegree_hash_map[i[0]] += 1
        for i in indegree_hash_map:
            if indegree_hash_map[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            e = queue.pop(0)
            result.append(e)
            for i in neighbours[e]:
                indegree_hash_map[i] -= 1
                if indegree_hash_map[i] == 0:
                    queue.append(i)
        length = len(result)
        if length == len(node_set):
            for i in range(numCourses):
                if i not in node_set:
                    result.append(i)
            return result
        else:
            return []
