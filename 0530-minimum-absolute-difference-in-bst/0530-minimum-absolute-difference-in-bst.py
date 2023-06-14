# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = 100001
        prev = 100001
        def inorder(root):
            nonlocal prev
            nonlocal minDiff
            if root:
                if root.left:
                    inorder(root.left)
                minDiff = min(abs(prev-root.val), minDiff)
                prev = root.val
                if root.right:
                    inorder(root.right)
        inorder(root)
        return minDiff