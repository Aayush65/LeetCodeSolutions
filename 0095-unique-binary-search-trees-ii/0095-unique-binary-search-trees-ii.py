# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def dfs(left: int, right: int) -> TreeNode:
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            res = []
            for i in range(left, right + 1):
                leftNodes = dfs(left, i - 1)
                rightNodes = dfs(i + 1, right)
                for l in leftNodes:
                    for r in rightNodes:
                        res.append(TreeNode(i, l, r))
            return res
        
        return dfs(1, n)