class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        newTree = [0] * n
    
        def traverse(index: int) -> int:
            if index > n:
                return 0
            newTree[index - 1] = cost[index - 1] + max(traverse(index * 2), traverse(index * 2 + 1))
            return newTree[index - 1]

        def calcIncrement(index: int, val) -> int:
            if index > n:
                return 0
            currIncrement = val - newTree[index - 1]
            leftChild = calcIncrement(index * 2, val - cost[index - 1] - currIncrement)
            rightChild = calcIncrement(index * 2 + 1, val - cost[index - 1] - currIncrement)
            return currIncrement + leftChild + rightChild

        val = traverse(1)
        return calcIncrement(1, val)