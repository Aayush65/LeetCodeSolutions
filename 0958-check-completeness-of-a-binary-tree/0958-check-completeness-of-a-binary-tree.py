# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        hasNone = False
        while level:
            nextLevel = []
            count = 0
            for i in level:
                if i:
                    nextLevel.append(i.left)
                    nextLevel.append(i.right)
                else:
                    hasNone = True
                if hasNone and i:
                    return False
            level = nextLevel
        return True     