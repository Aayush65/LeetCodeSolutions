# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        lot = []  # level order traversal
        row = [root]
        while row:
            nextRow = []
            rowVals = []
            for i in row:
                if i.left:
                    nextRow.append(i.left)
                if i.right:
                    nextRow.append(i.right)
                rowVals.append(i.val)
            lot.append(rowVals)
            row = nextRow
        
        def calcSwapsToSort(arr: list[int]) -> int:
            indices = {arr[i]: i for i in range(len(arr))}
            sortedArr = sorted(arr)
            swaps = 0
            for i in range(len(arr)):
                if arr[i] == sortedArr[i]:
                    continue
                arr[i], arr[indices[sortedArr[i]]] = arr[indices[sortedArr[i]]], arr[i]
                temp = indices[arr[i]]
                indices[arr[i]] = i
                indices[arr[temp]] = temp
                swaps += 1
            # print(arr)
            return swaps
            
        swaps = 0
        for i in lot:
            swaps += calcSwapsToSort(i)
        return swaps
                