# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = 0

        def traverse(node: TreeNode, minVal: int, maxVal: int) -> None:
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            nonlocal maxDiff
            diff = maxVal - minVal
            maxDiff = max(diff, maxDiff)
            if node.left:
                traverse(node.left, minVal, maxVal)
            if node.right:
                traverse(node.right, minVal, maxVal)
        
        traverse(root, root.val, root.val)
        return maxDiff