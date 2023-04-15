# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevelSum = root.val
        maxLevel = 1
        level = 1
        q = deque([root])
        while q:
            currLen = len(q)
            levelSum = 0
            for i in range(currLen):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                maxLevel = level
            level += 1
        return maxLevel