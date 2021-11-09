from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    if len(nums) == 0:
      return 0
    
    left = 0
    right = len(nums)-1

    while left <= right:
      mid = (left+right)//2
      print(f"mid:{mid} nums[mid]:{nums[mid]}")
      if nums[mid] >= target:
        print("right")
        right = mid-1
      else:
        print("left")
        left = mid+1
    
    return left

sol = Solution()
print(sol.searchInsert([1,3,5,6],0))
print(0)
print(sol.searchInsert([1,3,5,6],7))
print(4)
print(sol.searchInsert([1],0))
print(0)