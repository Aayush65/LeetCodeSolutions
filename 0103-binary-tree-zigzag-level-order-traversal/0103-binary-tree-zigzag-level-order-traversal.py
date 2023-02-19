# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root] if root else []
        res = [[root.val]] if stack else []
        isLeft = False
        while stack:
            nextLevel = []
            while stack:
                poped = stack.pop()
                if poped:
                    if isLeft:
                        if poped.left: nextLevel.append(poped.left)
                        if poped.right: nextLevel.append(poped.right)
                    else:
                        if poped.right: nextLevel.append(poped.right)
                        if poped.left: nextLevel.append(poped.left)
            stack = nextLevel
            isLeft = not isLeft
            if nextLevel:
                res.append([i.val for i in nextLevel])
        return res