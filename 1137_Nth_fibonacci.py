class Solution:
    def __init__(self):
      self.trib_cache = [-1 for _ in range(38)]
      self.trib_cache[0] = 0
      self.trib_cache[1] = 1
      self.trib_cache[2] = 1
        
    def tribonacci(self, n: int) -> int:
      if self.trib_cache[n] != -1:
        return self.trib_cache[n]

      self.trib_cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
      return self.trib_cache[n]


sol = Solution()
print(sol.tribonacci(4))
print(4)
print(sol.tribonacci(25))
print(1389537)