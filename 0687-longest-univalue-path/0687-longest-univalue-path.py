# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longestPath = 0
        
        def findLongestPath(node: TreeNode) -> list[int]:
            left = findLongestPath(node.left) if node.left else [0, 0]
            right = findLongestPath(node.right) if node.right else [0, 0]
            res = 1
            if node.val == left[0]:
                res += left[1]
            if node.val == right[0]:
                res += right[1]
            nonlocal longestPath
            longestPath = max(longestPath, res)
            
            if node.val == left[0] and node.val == right[0]:
                return [node.val, 1 + max(left[1], right[1])]
            if node.val == left[0]:
                return [node.val, 1 + left[1]]
            if node.val == right[0]:
                return [node.val, 1 + right[1]]
            return [node.val, 1]
        
        if not root:
            return 0
        findLongestPath(root)
        return longestPath - 1