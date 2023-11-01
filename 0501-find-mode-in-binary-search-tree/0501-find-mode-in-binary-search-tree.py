# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        iot = []
        def IOTraversal(node: TreeNode) -> list[int, set[int]]:
            if node.left:
                IOTraversal(node.left)
            iot.append(node.val)
            if node.right:
                IOTraversal(node.right)
                
        IOTraversal(root)
        
        maxFreq = freq = 0
        curr = iot[0]
        res = []
        for i in iot:
            if i != curr:
                curr = i
                freq = 0
            freq += 1
            if freq == maxFreq:
                res.append(curr)
            if freq > maxFreq:
                maxFreq = freq
                res = [curr]
        return res