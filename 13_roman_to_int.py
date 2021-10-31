from typing import List

class Solution:
  def romanToInt(self, s: str) -> int:
    s_list = list(s)
    result = 0
    before = "init"
    hashmap = {
      "init": 0,
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }
    for c in s_list:
      result += hashmap[c]
      if hashmap[before] < hashmap[c]:
        result -= hashmap[before]*2
      before = c
    return result

sol = Solution()
print(sol.romanToInt("III"))
print(3)
print(sol.romanToInt("IV"))
print(4)
print(sol.romanToInt("MCMXCIV"))
print(1994)