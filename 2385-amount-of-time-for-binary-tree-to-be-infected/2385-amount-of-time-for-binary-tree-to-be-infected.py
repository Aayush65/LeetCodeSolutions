# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
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
                
        q = [start] 
        infected = set()
        time = -1
        while q:
            newQ = []
            for node in q:
                infected.add(node)
                for nei in nodeMap[node]:
                    if nei in infected:
                        continue
                    newQ.append(nei)
            q = newQ
            time += 1
        return time