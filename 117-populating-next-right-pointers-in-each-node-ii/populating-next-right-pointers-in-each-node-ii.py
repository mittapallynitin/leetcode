"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        import collections 
        q = collections.deque()
        q.append(root)

        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                print(node.val)
                if prev:
                    prev.next = node
                    print(f"connecting {prev.val} to {node.val}")
                prev = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            node.next = None
        return root
