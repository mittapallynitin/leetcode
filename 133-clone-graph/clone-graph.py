"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node:
            return node

        q = deque([node])
        mapper = {node: Node(node.val)}
        while q:
            curr = q.popleft()
            for child in curr.neighbors:
                if child not in mapper:
                    mapper[child] = Node(child.val)
                    q.append(child)
                mapper[curr].neighbors.append(mapper[child])

        return  mapper[node]     