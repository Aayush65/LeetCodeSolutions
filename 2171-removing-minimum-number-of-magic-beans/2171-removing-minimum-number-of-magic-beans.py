class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        preSum = [0]
        for i in beans:
            preSum.append(preSum[-1] + i)
        
        removedBeans = sum(beans)
        for i in range(len(beans)):
            score = preSum[-1] - beans[i] * (len(beans) - i)
            removedBeans = min(removedBeans, score)
        return removedBeans 