# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        ans = []

        while q:

            elements = len(q)
            total = 0
            for _ in range(elements):
                node = q.pop(0)
                total += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(total / float(elements))
        
        return ans
            
