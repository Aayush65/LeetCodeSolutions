# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        serialisedMap = {}
        allDuplicates = set()
    
        def traverse(node: TreeNode):
            if not node:
                return ' N '
            serial =  ' ' + str(node.val) + ' ' + traverse(node.left) + ' ' + traverse(node.right) + ' '
            if serial in serialisedMap:
                allDuplicates.add(serialisedMap[serial])
            else:
                serialisedMap[serial] = node
            return serial
        
        traverse(root)
        return allDuplicates