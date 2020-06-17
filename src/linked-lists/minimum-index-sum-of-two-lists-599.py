class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sumValue = float("Inf")
        valueIndexlist = {}
        result = []
        for i in range(len(list1)):
          valueIndexlist[list1[i]] = i
        
        for i in range(len(list2)):
          if list2[i] in valueIndexlist:
            if i + valueIndexlist[list2[i]] < sumValue:
              sumValue = i + valueIndexlist[list2[i]]
              result = [list2[i]]
            elif i + valueIndexlist[list2[i]] == sumValue:
              result.append(list2[i])
        return result

            
if __name__ == "__main__":
    l = Solution()
    s1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    s2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    
        
          
