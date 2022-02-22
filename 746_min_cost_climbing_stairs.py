from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      if len(cost) == 2:
        return min(cost[0], cost[1])
      
      # 頂上はコスト0でOK
      cost.append(0)

      dp = {
        0: cost[0],
        1: cost[1]
      }
      for i,c in enumerate(cost[2:],2):
        dp[i] = min(dp[i-2]+c, dp[i-1]+c)

      print(dp)
      return dp[len(cost)-1]


sol = Solution()
print(sol.minCostClimbingStairs([10,15,20]))
print(15)
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(6)