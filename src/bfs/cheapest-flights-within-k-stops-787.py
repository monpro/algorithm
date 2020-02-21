class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        collect = collections.defaultdict(dict)
        heap = [(0, src, K + 1)]
        for i, j, p in flights:
            collect[i][j] = p
        while heap:
            currentDist, node, k = heapq.heappop(heap)
            if node == dst:
                return currentDist
            if k > 0:
                for j in collect[node]:
                    heapq.heappush(heap, (currentDist + collect[node][j], j, k - 1))
        return -1
    