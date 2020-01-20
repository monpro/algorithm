class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        evenCost = 0
        oddCost = 0
        for i in chips:
            if i % 2 == 0:
                evenCost += 1
            else:
                oddCost += 1
        
        return min(evenCost, oddCost)