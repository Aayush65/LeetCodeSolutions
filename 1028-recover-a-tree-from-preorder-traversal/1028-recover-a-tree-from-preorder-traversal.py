# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        preorder = []
        while i < len(traversal):
            level = 0
            while traversal[i] == '-':
                level += 1
                i += 1
            num = 0
            while i < len(traversal) and traversal[i] != '-':
                num = num * 10 + int(traversal[i])
                i += 1
            preorder.append((num, level))
        preorder.reverse()

        def makeTree(depth: int) -> TreeNode:
            if not preorder or preorder[-1][1] != depth:
                return None
            val, d = preorder.pop()
            root = TreeNode(val)
            root.left = makeTree(depth + 1)
            root.right = makeTree(depth + 1)
            return root
        
        return makeTree(0)