from typing import List

class Solution:
	def isPalindrome(self, x: int) -> bool:
		x_list = list(str(x))
		for i in range(len(x_list)):
			j = len(x_list)-1 - i
			if i >= j:
				break
			if x_list[i] != x_list[j]:
				return False
		return True


sol = Solution()
print(sol.isPalindrome(121))
print(True)
print(sol.isPalindrome(-121))
print(False)