# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iot = self.inorder(root)
        self.ptr = -1
    
    def inorder(self, root: Optional[TreeNode]):
        iot = []
        if root:
            iot += self.inorder(root.left)
            iot.append(root)
            iot += self.inorder(root.right)
        return iot
        
    def next(self) -> int:
        self.ptr += 1
        return self.iot[self.ptr].val
        
    def hasNext(self) -> bool:
        return self.ptr + 1 < len(self.iot)            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()