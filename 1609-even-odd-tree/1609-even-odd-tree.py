# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = []
        level = [root]
        while level:
            nextLevel = []
            levels.append([])
            for i in level:
                levels[-1].append(i.val)
                if i.left:
                    nextLevel.append(i.left)
                if i.right:
                    nextLevel.append(i.right)
            level = nextLevel

        def isIncreasing(arr: List[int]) -> bool:
            prev = 0
            for i in arr:
                if i <= prev or not i % 2:
                    return False
                prev = i
            return True

        def isDecreasing(arr: List[int]) -> bool:
            prev = 10000000
            for i in arr:
                if i >= prev or i % 2:
                    return False
                prev = i
            return True

        for i in range(len(levels)):
            if i % 2:
                if not isDecreasing(levels[i]):
                    print(levels[i])
                    return False
            else:
                if not isIncreasing(levels[i]):
                    print(levels[i])
                    return False
        return True

