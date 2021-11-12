class Solution:
    def __init__(self):
      self.fib_cache = [-1 for _ in range(3)]
      self.fib_cache[0] = 0
      self.fib_cache[1] = 1
        
    def fib(self, n: int) -> int:
      if self.fib_cache[n] != -1:
        return self.fib_cache[n]

      self.fib_cache[n] = self.fib(n-1) + self.fib(n-2)
      return self.fib_cache[n]


sol = Solution()
print(sol.fib(4))
print(3)
print(sol.fib(3))
print(2)