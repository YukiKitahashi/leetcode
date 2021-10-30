from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		hashmap = dict()
		result = [-1, -1]
		for i in range(len(nums)):
			remain = target - nums[i]
			if remain in hashmap:
				result = [hashmap[remain],i]
				break
			else:
				hashmap[nums[i]] = i
		return result


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print([0,1])