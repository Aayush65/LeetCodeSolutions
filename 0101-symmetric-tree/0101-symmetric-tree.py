# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(root1: TreeNode, root2: TreeNode) -> bool:
            res = True
            if not root1 and not root2:
                return res
            if (root1 and not root2) or (not root1 and root2):
                return False
            if root1.val == root2.val:
                if root1.left or root2.right:
                    res &= isMirror(root1.left, root2.right)
                if root1.right or root2.left:
                    res &= isMirror(root1.right, root2.left)
            else:
                return False
            return res
        return isMirror(root.left, root.right)