# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [(root, 0)]
        result = []
        max_width = 0
        while q:
            level = []
            for _ in range(len(q)):
                node, pos = q.pop(0)
                level.append((node.val,pos))
                if node.left: q.append((node.left, pos-1))
                if node.right: q.append((node.right, pos+1))
            result.append(level[::])

        vals = {}
        for level in result:
            for node, pos in level:
                vals[pos] = vals.get(pos, []) + [node]
        
        return [v for k, v in sorted(vals.items())]


