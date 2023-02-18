# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        newRoot = TreeNode(root.val)
        newTree = [newRoot]
        level = [root]
        while level:
            newLevel = []
            for i in range(len(level)):
                if not level[i].left:
                    break
                newLevel.append(level[i].left)
                newLevel.append(level[i].right)
            level = newLevel
            if newLevel and int(log2(len(newLevel))) % 2:
                tempLevel = level[::-1]
            else:
                tempLevel = level
            newLevel = []
            for i in range(0, len(tempLevel), 2):
                newTree[i // 2].left = TreeNode(tempLevel[i].val)
                newTree[i // 2].right = TreeNode(tempLevel[i + 1].val)
                newLevel.append(newTree[i // 2].left)
                newLevel.append(newTree[i // 2].right)
            newTree = newLevel
        return newRoot