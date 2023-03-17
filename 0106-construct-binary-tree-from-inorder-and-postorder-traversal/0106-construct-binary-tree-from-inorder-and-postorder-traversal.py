# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        hm = {inorder[i]: i for i in range(n)}
    
        def makeTree(i: int, j: int) -> TreeNode:
            if j < i:
                return None
            root = TreeNode(postorder[-1])
            rootIndex = hm[postorder.pop()]
            root.right = makeTree(rootIndex + 1, j)
            root.left = makeTree(i, rootIndex - 1)
            return root
        
        return makeTree(0, n - 1)