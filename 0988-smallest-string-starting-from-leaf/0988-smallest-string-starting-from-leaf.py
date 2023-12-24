# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return []
            allS = dfs(node.left)
            allS.extend(dfs(node.right))
            val = chr(node.val + ord('a'))
            for i in allS:
                i.append(val)
            if not allS:
                allS.append([val])
            return allS
        
        allS = dfs(root)
        minS = ''.join(allS[0])
        for i in allS:
            minS = min(minS, ''.join(i))
        return minS