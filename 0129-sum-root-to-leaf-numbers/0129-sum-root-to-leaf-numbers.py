# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        allNumbers = 0

        def traverse(root: TreeNode, val: int = 0) -> None:
            val = val * 10 + root.val

            if not root.left and not root.right:
                nonlocal allNumbers
                allNumbers += val
            if root.left:
                traverse(root.left, val)
            if root.right:
                traverse(root.right, val)

        traverse(root)
        return allNumbers