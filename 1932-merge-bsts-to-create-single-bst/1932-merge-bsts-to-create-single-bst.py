# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        nodeMap = {tree.val: tree for tree in trees}
        nodes = set()
        for node in trees:
            nodes.add(node.val)
            if node.left:
                nodes.add(node.left.val)
                if node.left.val in nodeMap:
                    node.left = nodeMap[node.left.val]
                    del nodeMap[node.left.val]
            if node.right:
                nodes.add(node.right.val)
                if node.right.val in nodeMap:
                    node.right = nodeMap[node.right.val]
                    del nodeMap[node.right.val]
            
        if len(nodeMap) != 1:
            return None
        for i in nodeMap:
            root = nodeMap[i]
        
        traversal = []
        def iot(node: TreeNode) -> None:
            if node.left:
                iot(node.left)
            traversal.append(node.val)
            if node.right:
                iot(node.right)
        iot(root)
        if len(traversal) != len(nodes):
            return None
        
        for i in range(1, len(traversal)):
            if traversal[i] <= traversal[i - 1]:
                return None
        return root