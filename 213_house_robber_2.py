from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
      if nums == None or len(nums) == 0:
        return 0
      if len(nums) == 1:
        return nums[0]

      top_dp = self.dp(nums[:-1])
      tail_dp = self.dp(nums[1:])

      return max(top_dp, tail_dp)


    def dp(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return nums[0]

      dp = {
        0: nums[0],
        1: max(nums[0], nums[1])
      }

      for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

      return dp[len(nums)-1]

sol = Solution()
print(sol.rob([1,2,3,1]))
print(4)
print(sol.rob([2,3,2]))
print(3)
print(sol.rob([1,2,3]))
print(3)