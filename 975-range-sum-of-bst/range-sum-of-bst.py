# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        vals = []

        q = [root]
        while q:
            node = q.pop(0)
            if low <= node.val <= high:
                vals.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return sum(vals)
        