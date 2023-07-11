# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        nodeMap = {root.val: []}
        q = deque([root])
        while q:
            poped = q.popleft()
            if poped.left:
                nodeMap[poped.left.val] = [poped.val]
                nodeMap[poped.val].append(poped.left.val) 
                q.append(poped.left)
            if poped.right:
                nodeMap[poped.right.val] = [poped.val]
                nodeMap[poped.val].append(poped.right.val)
                q.append(poped.right)
                
        q = [target.val] 
        visited = set()
        for step in range(k):
            if not q:
                break
            newQ = []
            for node in q:
                visited.add(node)
                for nei in nodeMap[node]:
                    if nei in visited:
                        continue
                    newQ.append(nei)
            q = newQ
        return q