# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        to_delete.append(-1)
        to_delete = set(to_delete)
        dummy = TreeNode(-1, root)
        def dfs(root: TreeNode) -> None:
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            if root.left and root.left.val == -1:
                root.left = None
            if root.right and root.right.val == -1:
                root.right = None
            if root.val in to_delete:
                to_delete.remove(root.val)
                root.val = -1
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)

        dfs(dummy)
        return forest