# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def height(root, dir):
            h = 0
            while root:
                h += 1
                if dir == "left":
                    root = root.left
                else: 
                    root = root.right
            return h
        
        lh = height(root, "left")
        rh = height(root, "right")

        if lh == rh:
            return 2**lh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        