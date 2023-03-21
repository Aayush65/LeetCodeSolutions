# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def canBePalindrome(arr: list[int]) -> int:
            n = 0
            # print(arr)
            for i in arr:
                if i: n += i
            isAllowed = False
            if n % 2:
                isAllowed = True
            for i in arr:
                if i % 2:
                    if isAllowed:
                        isAllowed = False
                    else:
                        return 0
            return 1
        
        vals = [0] * 10
        def traverse(node: TreeNode) -> int:
            res = 0
            vals[node.val] += 1
            if not node.left and not node.right:
                res += canBePalindrome(vals)
            if node.left:
                res += traverse(node.left)
            if node.right:
                res += traverse(node.right)
            vals[node.val] -= 1
            return res

        return traverse(root)