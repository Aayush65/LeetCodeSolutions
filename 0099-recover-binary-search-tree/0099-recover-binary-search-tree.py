# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        iot = []
        def inorder(node: TreeNode) -> None:
            if node.left:
                inorder(node.left)
            iot.append(node)
            if node.right:
                inorder(node.right)
        
        inorder(root)
        toBeSwapped = []
        for i in range(len(iot) - 1):
            if iot[i].val > iot[i + 1].val:
                if toBeSwapped:
                    toBeSwapped[1] = iot[i + 1]
                else:
                    toBeSwapped = [iot[i], iot[i + 1]]
        
        a, b = toBeSwapped
        a.val, b.val = b.val, a.val