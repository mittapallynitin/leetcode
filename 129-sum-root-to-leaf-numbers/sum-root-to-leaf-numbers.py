# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        def dfs(node, value):
            if not node:
                return
            
            if not node.left and not node.right:
                nums.append(value * 10 + node.val )
            
            value *= 10
            dfs(node.left, value + int(node.val))
            dfs(node.right, value + int(node.val))
    
        dfs(root, 0)
        return sum(nums)

        