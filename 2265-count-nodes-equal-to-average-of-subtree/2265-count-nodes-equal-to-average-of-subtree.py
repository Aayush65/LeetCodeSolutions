# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def traverse(node: TreeNode) -> list[int]:
            if not node:
                return [0, 0]
            avg = [node.val, 1]
            avgLeft = traverse(node.left)
            avgRight = traverse(node.right)
            avg[0] += avgLeft[0] + avgRight[0]
            avg[1] += avgLeft[1] + avgRight[1]
            if node.val == avg[0] // avg[1]:
                nonlocal count
                count += 1
            return avg            
            
        traverse(root)
        return count