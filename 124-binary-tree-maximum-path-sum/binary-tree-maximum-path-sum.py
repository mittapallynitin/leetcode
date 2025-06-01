# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Consider the node as root
            self.res = max(
                self.res, 
                node.val, 
                node.val + left_sum, 
                node.val + right_sum, 
                node.val + left_sum + right_sum,
            )

            # If this is a passing node i.e left_sum or right_sum
            return max(
                node.val, 
                node.val + left_sum,
                node.val + right_sum
            )
            
        dfs(root)
        return self.res
        

        