class Solution:
    def climbStairs(self, n: int) -> int:
      if n == 1:
        return 1

      dp = [1]
      for i in range(1, n+1):
        r = dp[-1]
        if i > 1:
          r += dp[-2]
        dp.append(r)

      return dp[-1]

sol = Solution()
print(sol.climbStairs(4))
print(5)
print(sol.climbStairs(3))
print(3)