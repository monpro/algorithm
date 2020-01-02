import collections

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start >= 0 and start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            if arr[start] == 0:
                return True
            else:
                return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        
        return False

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = collections.deque([start])
        while len(queue) > 0:
            i = queue.popleft()
            if i >= 0 and i < n:
                if arr[i] == 0:
                    return True
                if i - arr[i] not in visited:
                    visited.add(i - arr[i])
                    queue.append(i - arr[i])
                if i + arr[i] not in visited:
                    visited.add(i + arr[i])
                    queue.append(i + arr[i])
        return False