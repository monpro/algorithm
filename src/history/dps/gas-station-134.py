class Solution:
    def canCompleteCircuit(self, gas, cost):
      # use brute force
      tank, total, start = 0, 0, 0
      for i in range(len(gas)):
        current = gas[i] - cost[i]
        tank += current
        total += current
        if tank < 0:
          start = i + 1
          tank = 0
      
      if total < 0:
        return -1
      else:
        return start






if __name__ == "__main__":
    l = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(l.canCompleteCircuit(gas, cost))
        