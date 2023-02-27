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

        def making(i: int, j: int, n: int) -> None:
            node = Node(grid[i][j], True)
            for x in range(i, i + n):
                for y in range(j, j + n):
                    if grid[x][y] != grid[i][j]:
                        node.isLeaf = False
                        break
                    if not node.isLeaf:
                        break
            
            if not node.isLeaf:
                node.topLeft = making(i, j, n // 2)
                node.topRight = making(i, j + n // 2, n // 2)
                node.bottomLeft = making(i + n // 2, j, n // 2)
                node.bottomRight = making(i + n // 2, j + n // 2, n // 2)
            return node

        return making(0, 0, len(grid))