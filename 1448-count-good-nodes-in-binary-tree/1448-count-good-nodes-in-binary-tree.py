# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(node: TreeNode, maxNode: int) -> int:
            if not node:
                return 0
            res = 0
            if node.val >= maxNode:
                res = 1
                maxNode = node.val
            res += traverse(node.left, maxNode) + traverse(node.right, maxNode)
            return res

        return traverse(root, -float("inf"))