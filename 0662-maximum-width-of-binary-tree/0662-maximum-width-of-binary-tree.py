# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen = 1 if root else 0
        level = deque([[root]])
        while level:
            elements = 0
            for i in level:
                if len(i) == 2:
                    elements += i[1]
                else:
                    elements += 1

            maxLen = max(elements, maxLen)
            n = len(level)
            for i in range(n):
                if len(level[0]) == 2 and level[0][0] == None:
                    level.append([None, level[0][1] * 2])
                else:
                    level.append([level[0][0].left] if level[0][0].left else [None, 1])
                    level.append([level[0][0].right] if level[0][0].right else [None, 1])
                level.popleft()

            while level and len(level[-1]) == 2:
                level.pop()
            while level and len(level[0]) == 2:
                level.popleft()
        return maxLen