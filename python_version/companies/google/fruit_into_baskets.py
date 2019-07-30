class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # find longest subarray with two distinct elements
        current_window = dict()
        left, result = 0,0
        for i, j in enumerate(tree):
            current_window[j] = current_window.get(j,0) + 1
            while len(current_window) > 2:
                current_window[tree[left]] -= 1
                if current_window[tree[left]] == 0:
                    del current_window[tree[left]]
                left += 1
            result = max(result,i - left + 1)

        return result


