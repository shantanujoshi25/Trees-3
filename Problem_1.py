# // Time Complexity : O(n)
# // Space Complexity : O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        self.result = []

        def helper(root,path,pathSum):
           
            if(root.left is None and root.right is None):
                if(pathSum == targetSum):
                    self.result.append(path.copy())

            if(root.left):
                path.append(root.left.val)
                helper(root.left,path,pathSum+root.left.val)
                path.pop()
            if(root.right):
                path.append(root.right.val)
                helper(root.right,path,pathSum+root.right.val)
                path.pop()
            



        if(root is not None):
            helper(root,[root.val],root.val)
        return self.result