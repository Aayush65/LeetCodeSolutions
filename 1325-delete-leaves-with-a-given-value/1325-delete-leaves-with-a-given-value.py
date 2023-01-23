# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = curr = TreeNode(None, root)
        
        def leafDeletion(node: TreeNode, par: TreeNode, isLeft) -> None:
            if node.left:
                leafDeletion(node.left, node, True)
            if node.right:
                leafDeletion(node.right, node, False)
            if not node.left and not node.right and node.val == target:
                if isLeft:
                    par.left = None
                else:
                    par.right = None
            
        leafDeletion(root, curr, True)
        return dummy.left