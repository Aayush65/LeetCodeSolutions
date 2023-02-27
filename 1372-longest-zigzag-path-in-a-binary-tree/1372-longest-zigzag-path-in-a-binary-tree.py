# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def traverse(node: TreeNode, isLeft: bool) -> int:
            if (node, isLeft) in memo:
                return memo[(node, isLeft)]
            res = 1
            if isLeft and node.left:
                res += traverse(node.left, not isLeft)
            elif not isLeft and node.right:
                res += traverse(node.right, not isLeft)
            memo[(node, isLeft)] = res
            return res

        maxPath = 1
        nodes = [root]
        while nodes:
            nextNodes = []
            for i in nodes:
                maxPath = max(maxPath, traverse(i, True), traverse(i, False))
                if i.left:
                    nextNodes.append(i.left)
                if i.right:
                    nextNodes.append(i.right)
            nodes = nextNodes
        return maxPath - 1