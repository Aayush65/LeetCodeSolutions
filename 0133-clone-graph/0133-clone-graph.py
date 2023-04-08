"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes = {}

        def dfs(vertice: Node):
            if vertice.val in nodes:
                return nodes[vertice.val]
            newVertice = Node(vertice.val, [])
            nodes[vertice.val] = newVertice
            for i in vertice.neighbors:
                newVertice.neighbors.append(dfs(i))
            return newVertice
        if node:
            dfs(node)
        return nodes[1] if 1 in nodes else None