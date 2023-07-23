# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def backtrack(n: int) -> list[TreeNode]:
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            res = []
            for left in range(1, n, 2):
                right = n - left - 1
                leftTrees, rightTrees = backtrack(left), backtrack(right)
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        res.append(TreeNode(0, leftTree, rightTree))
            return res
        
        return backtrack(n)