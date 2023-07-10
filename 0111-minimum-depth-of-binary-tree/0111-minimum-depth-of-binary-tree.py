# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        left = 100001
        right = 100001
        if root:
            if root.left:
                left = self.minDepth(root.left)
            if root.right:
                right = self.minDepth(root.right)
            if not root.left and not root.right:
                return 1
            depth = 1 + min(left, right)
        return depth