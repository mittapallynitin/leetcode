# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, node: Optional[TreeNode], targetSum: int) -> bool:

        
        if not node:
            return False
        
        if not node.left and not node.right:
            return node.val == targetSum

        return (
            self.hasPathSum(node.left, targetSum - node.val) or 
            self.hasPathSum(node.right, targetSum - node.val)
        )
        