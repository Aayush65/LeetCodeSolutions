# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pruning(node: TreeNode) -> None:
            if node.left:
                pruning(node.left)
            if node.right:
                pruning(node.right)
            if node.left and node.left.val == -1:
                node.left = None
            if node.right and node.right.val == -1:
                node.right = None
            if not node.val and not node.left and not node.right:
                node.val = -1
        
        dummy = TreeNode(-1, root)
        pruning(dummy)
        return dummy.left