
class Solution:
    def isValid(self, s: str) -> bool:
      hashmap = {
        "(":1,
        "{":2,
        "[":3,
        "]":-3,
        "}":-2,
        ")":-1
      }
      seq = []
      for i in range(len(s)):
        if s[i] not in hashmap:
          return False
        # 開く方では順序を蓄積
        if hashmap[s[i]] > 0:
          seq.append(hashmap[s[i]])
        # 閉じる方では順序通りかチェック
        else:
          if len(seq) == 0:
            return False
          if seq.pop(-1) + hashmap[s[i]] != 0:
            return False

      return len(seq) == 0

sol = Solution()
print(sol.isPalindrome(121))
print(True)
print(sol.isPalindrome(-121))
print(False)