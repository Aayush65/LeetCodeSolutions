class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        maxSum = 0
        for i in range(n):
            currSum = maxHeights[i]
            prev = maxHeights[i]
            for j in range(i - 1, -1, -1):
                if maxHeights[j] <= prev:
                    currSum += maxHeights[j]
                else:
                    currSum += prev
                prev = min(maxHeights[j], prev)
                
            prev = maxHeights[i]
            for j in range(i + 1, n):
                if maxHeights[j] <= prev:
                    currSum += maxHeights[j]
                else:
                    currSum += prev
                prev = min(maxHeights[j], prev)
            maxSum = max(maxSum, currSum)
        return maxSum