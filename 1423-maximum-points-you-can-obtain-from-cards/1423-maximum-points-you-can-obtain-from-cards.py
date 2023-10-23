class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        preSum = [0]
        for i in cardPoints:
            preSum.append(preSum[-1] + i)
        
        k = len(cardPoints) - k
        minWindow = preSum[-1]
        for i in range(len(cardPoints) - k + 1):
            window = preSum[i + k] - preSum[i]
            minWindow = min(minWindow, window)
        
        return preSum[-1] - minWindow