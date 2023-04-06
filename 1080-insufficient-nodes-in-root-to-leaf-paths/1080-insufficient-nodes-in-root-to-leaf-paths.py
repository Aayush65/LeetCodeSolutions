# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
            
        isLeaf = lambda x: not x.left and not x.right
        
        def traverse(node: TreeNode, currLmt: int) -> bool:
            if not node:
                return currLmt < 1
            if isLeaf(node):
                return currLmt - node.val < 1
            
            trimLeft = False
            trimRight = False
            if node.left:
                trimLeft = traverse(node.left, currLmt - node.val)
            if node.right:
                trimRight = traverse(node.right, currLmt - node.val)
            
            if not trimLeft:
                node.left = None
            if not trimRight:
                node.right = None
            return trimLeft or trimRight
            
        return root if traverse(root, limit) else None