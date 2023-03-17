# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        preorder.reverse()
        hm = {inorder[i]: i for i in range(n)}

        def makeTree(i: int, j: int) -> TreeNode:
            if j < i:
                return None
            root = TreeNode(preorder[-1])
            rootIndex = hm[preorder.pop()]
            root.left = makeTree(i, rootIndex - 1)
            root.right = makeTree(rootIndex + 1, j)
            return root
        
        return makeTree(0, n - 1)