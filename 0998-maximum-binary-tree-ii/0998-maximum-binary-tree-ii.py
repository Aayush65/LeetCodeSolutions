# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = TreeNode(None, None, root)
        curr = dummy
        while curr.right and curr.right.val > val:
            curr = curr.right
        curr.right = TreeNode(val, curr.right)
        return dummy.right