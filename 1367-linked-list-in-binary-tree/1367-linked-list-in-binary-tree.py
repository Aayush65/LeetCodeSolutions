# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        @cache
        def traverse(nodeTree: TreeNode, nodeList: ListNode) -> bool:
            if not nodeList:
                return True
            if not nodeTree:
                return False
            res = False
            if nodeTree.val == nodeList.val:
                res = traverse(nodeTree.left, nodeList.next) or traverse(nodeTree.right, nodeList.next)
            if nodeTree.val == head.val and not res:
                res = traverse(nodeTree.left, head.next) or traverse(nodeTree.right, head.next)
            if not res:
                return traverse(nodeTree.left, head) or traverse(nodeTree.right, head)
            return res
            
        return traverse(root, head)