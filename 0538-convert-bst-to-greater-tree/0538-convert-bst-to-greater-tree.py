# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        
        def inorderTraversal(node: TreeNode) -> None:
            if not node:
                return
            inorderTraversal(node.right)
            nodes.append(node)
            inorderTraversal(node.left)
        
        inorderTraversal(root)
        
        prefix = []
        for node in nodes:
            if not prefix:
                prefix.append(node.val)
            else:
                prefix.append(node.val + prefix[-1])
            node.val = prefix[-1]
        return root