# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.nodeSet = set()
        self.recover(root)
        
    def recover(self, root: TreeNode) -> set[int]:
        self.nodeSet.add(root.val)
        if root.left:
            root.left.val = root.val * 2 + 1
            self.recover(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.recover(root.right)
        
    def find(self, target: int) -> bool:
        return target in self.nodeSet


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)