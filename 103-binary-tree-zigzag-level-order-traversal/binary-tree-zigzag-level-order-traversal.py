# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [root]
        output = []
        i = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            if i % 2 == 0:
                output.append(level)
            else:
                output.append(level[::-1])
            i += 1
        return output