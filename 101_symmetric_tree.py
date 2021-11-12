# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      if root == None:
        return True
      
      return self.compare(root.left, root.right)
      
      return True

    def compare(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
      if left == None and right == None:
        return True
      elif left == None or right == None:
        return False
      elif left.val != right.val:
        return False
      
      return self.compare(left.left, right.right) and self.compare(left.right, right.left)


      