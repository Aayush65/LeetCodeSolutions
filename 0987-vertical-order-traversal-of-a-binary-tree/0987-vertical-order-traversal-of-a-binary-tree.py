# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        xAxis = {}
        minX = 0
        maxX = 0

        # DFS implementation
        # def traversal(node: TreeNode, x: int, y: int) -> None:
        #     nonlocal minX
        #     nonlocal maxX
        #     minX = min(minX, x)
        #     maxX = max(maxX, x)

        #     if x in xAxis:
        #         xAxis[x].append([y, node.val])
        #     else:
        #         xAxis[x] = [[y, node.val]]
        #     if node.left:
        #         traversal(node.left, x - 1, y + 1)
        #     if node.right:
        #         traversal(node.right, x + 1, y + 1)
        # traversal(root, 0, 0)

        # BFS implenmentation
        q = [[root, 0]]
        y = 0
        while q:
            newQ = []
            for i, x in q:
                minX = min(minX, x)
                maxX = max(maxX, x)
                if x in xAxis:
                    xAxis[x].append([y, i.val])
                else:
                    xAxis[x] = [[y, i.val]]
                if i.left:
                    newQ.append([i.left, x - 1])
                if i.right:
                    newQ.append([i.right, x + 1])
            q = newQ
            y += 1

        vlot = []
        for i in range(minX, maxX + 1):
            level = []
            xAxis[i].sort()
            for j in xAxis[i]:
                level.append(j[1])
            vlot.append(level)
        return vlot