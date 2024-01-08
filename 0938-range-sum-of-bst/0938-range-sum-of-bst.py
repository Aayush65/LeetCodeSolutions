# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = 0
        if low <= root.val <= high:
            rangeSum = root.val
        if root.left:
            rangeSum += self.rangeSumBST(root.left, low, high)
        if root.right:
            rangeSum += self.rangeSumBST(root.right, low, high)
        return rangeSum