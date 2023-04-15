# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = deque([root])
        while q:
            level = []
            levelSum = 0
            currLen = len(q)
            for i in range(currLen):
                node = q.popleft()
                if node.left or node.right:
                    level.append([])
                if node.left:
                    levelSum += node.left.val
                    level[-1].append(node.left)
                    q.append(node.left)
                if node.right:
                    levelSum += node.right.val
                    level[-1].append(node.right)
                    q.append(node.right)
            
            for brothers in level:
                broVal = levelSum - sum([i.val for i in brothers])
                for i in brothers:
                    i.val = broVal
        return root