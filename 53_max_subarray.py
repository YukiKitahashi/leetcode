from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    local_max = nums[0]
    result = nums[0]

    for num in nums[1:]:
      # local_maxは現時点までで一番大きいsubarrayの和
      # 現在の最大値に次の値を足すのが良いか(=1つ前からの連続期間)次の値をsubarrayの起点にするのがいいのか判断
      local_max = max(local_max+num, num)
      # 過去の最大値と現在有望なsubarrayのどちらが大きいか判断
      result = max(result, local_max)
    return result

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(6)
print(sol.maxSubArray([-2,-1]))
print(-1)
print(sol.maxSubArray([5,4,-1,7,8]))
print(23)