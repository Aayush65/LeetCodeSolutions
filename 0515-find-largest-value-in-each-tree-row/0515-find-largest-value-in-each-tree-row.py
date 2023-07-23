# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        
        while q and root:
            newQ = []
            maxVal = -float("inf")
            for node in q:
                if not node:
                    continue
                maxVal = max(node.val, maxVal)
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
            q = newQ
            res.append(maxVal)
        return res