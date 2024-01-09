# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaf(root: TreeNode) -> list[int]:
            leaf = []
            if not root.left and not root.right:
                leaf.append(root.val)
            else:
                if root.left:
                    leaf += findLeaf(root.left)
                if root.right:
                    leaf += findLeaf(root.right)
            return leaf

        return findLeaf(root1) == findLeaf(root2)