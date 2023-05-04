# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [root]
        par = {root: None}
        while level:
            newLevel = []
            for i in level:
                if i.left:
                    par[i.left] = i
                    newLevel.append(i.left)
                if i.right:
                    par[i.right] = i
                    newLevel.append(i.right)
            if not newLevel:
                break
            level = newLevel
        
        while len(level) > 1:
            parLevel = set()
            for i in level:
                parLevel.add(par[i])
            level = parLevel
        
        return level.pop()