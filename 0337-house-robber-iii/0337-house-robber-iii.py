# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root: Optional[TreeNode], canRob: bool = True) -> int:
        if not root:
            return 0
        robbed = self.rob(root.left, True) + self.rob(root.right, True)
        if canRob:
            robbed = max(robbed, root.val + self.rob(root.left, False) + self.rob(root.right, False))
        return robbed