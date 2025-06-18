# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        greater = float("inf")
        lesser = float("-inf")

        def search(node):
            if not node:
                return 
            
            nonlocal greater, lesser

            if target <= node.val < greater:
                greater = node.val
            
            if lesser < node.val <= target:
                lesser = node.val
            
            search(node.left)
            search(node.right)

        search(root)
        gd = greater - target
        ld = target - lesser
        print(lesser, greater)
        if gd < ld:
            return greater
        else:
            return lesser