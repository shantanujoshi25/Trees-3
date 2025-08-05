# // Time Complexity : O(n)
# // Space Complexity : O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.sym = True

        def helper(left,right):
            if(left is None and right is None):
                return None
            if(left is None or right is None):
                self.sym = False
                return None
            if(left.val != right.val):
                self.sym = False
                return None
            helper(left.left,right.right)
            helper(left.right,right.left)
                
        helper(root.left,root.right)
        return self.sym 
        