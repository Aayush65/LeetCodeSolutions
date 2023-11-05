# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        nodeMap = {i + 1: set() for i in range(n)}

        def traverse(node: int) -> None:
            if node.left:
                nodeMap[node.val].add(node.left.val)
                nodeMap[node.left.val].add(node.val)
                traverse(node.left)
            if node.right:
                nodeMap[node.val].add(node.right.val)
                nodeMap[node.right.val].add(node.val)
                traverse(node.right)

        traverse(root)

        visited = set()
        def findTreeLen(node: int) -> bool:
            if node in visited: return 0
            visited.add(node)
            res = 1
            for nei in nodeMap[node]:
                res += findTreeLen(nei)
            visited.remove(node)
            return res

        neighbours = nodeMap[x]
        for nei in neighbours:
            nodeMap[nei].remove(x)
            nodeMap[x].remove(nei)
            if findTreeLen(nei) > n / 2: return True
            nodeMap[nei].add(x)
            nodeMap[x].add(nei)

        return False