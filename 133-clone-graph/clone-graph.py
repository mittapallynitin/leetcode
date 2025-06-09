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
        root = node
        q = deque([node])
        mapper = {}
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    mapper[node] = Node(node.val)
                    for child in node.neighbors:
                        if child and child not in mapper: q.append(child)

        for orginal, copy in mapper.items():
            for ch in orginal.neighbors:
                copy.neighbors.append(mapper[ch])

        return  mapper[root]     