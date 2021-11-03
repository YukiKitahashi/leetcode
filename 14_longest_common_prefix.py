from typing import List
import sys

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      result = ""
      for i, s in enumerate(strs):
        if i == 0:
          result = s
          continue
        while not s.startswith(result):
          result = result[:-1]
      return result

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print("fl")
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print("")
print(sol.longestCommonPrefix(["cir","car"]))
print("c")