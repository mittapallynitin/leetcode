"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid) - 1
        
        def allEqual(startRow, endRow, startCol, endCol) -> bool:
            val = 0
            for i in range(startRow, endRow + 1):
                for j in range(startCol, endCol + 1):
                    val += grid[i][j]
            return val / (endRow - startRow + 1) **2
        
        def build(startRow, endRow, startCol, endCol) -> 'Node':
            val = allEqual(startRow, endRow, startCol, endCol)
            if val in [1, 0]:
                node = Node(val, 1, None, None, None, None)
            else:
                node = Node(1, 0, None, None, None, None)
                midRow = (endRow + startRow) // 2
                midCol = (endCol + startCol) // 2
                node.topLeft = build(startRow, midRow, startCol, midCol)
                node.topRight = build(startRow, midRow, midCol + 1, endCol)
                node.bottomLeft = build(midRow+1, endRow, startCol, midCol)
                node.bottomRight = build(midRow+1, endRow ,  midCol + 1, endCol)
            return node
        
        return build(0, n, 0, n)

                    