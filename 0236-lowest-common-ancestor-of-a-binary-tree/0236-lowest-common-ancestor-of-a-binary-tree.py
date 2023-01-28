# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(root:TreeNode, target:TreeNode) -> list[TreeNode]:
            if root == target:
                return [target]
            res = []
            if root.left:
                res = path(root.left, target)
                if res:
                    res.append(root)
                    return res
            if root.right:
                res = path(root.right, target)
                if res:
                    res.append(root)
                    return res
            return res
        
        path1 = set(path(root, p))
        path2 = path(root, q)
        for i in path2:
            if i in path1:
                return i