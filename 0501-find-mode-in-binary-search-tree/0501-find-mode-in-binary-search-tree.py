# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        iot = []
        def IOTraversal(node: TreeNode) -> None:
            if node.left:
                IOTraversal(node.left)
            iot.append(node.val)
            if node.right:
                IOTraversal(node.right)
        IOTraversal(root)
        
        freq = {i: 0 for i in iot}
        for i in iot:
            freq[i] += 1
        
        maxApp = 0
        mode = [iot[0]]
        for i in freq:
            if maxApp < freq[i]:
                maxApp = freq[i]
                mode = [i]
            elif maxApp == freq[i]:
                mode.append(i)
        return mode