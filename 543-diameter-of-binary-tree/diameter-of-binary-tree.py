# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = float("-inf")

        def dfs(node):
            if not node:
                return 0

            nonlocal longest
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Consider passing through the node
            longest = max(longest, left_depth + right_depth)

            # Consider for up stream
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return longest
        