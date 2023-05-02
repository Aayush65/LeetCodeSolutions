class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroSum = [0]
        for i in nums:
            if not i:
                zeroSum.append(zeroSum[-1] + 1)
            else:
                zeroSum.append(zeroSum[-1])

        oneSum = [0]
        for i in nums[::-1]:
            if i:
                oneSum.append(oneSum[-1] + 1)
            else:
                oneSum.append(oneSum[-1])
        oneSum.reverse()

        res = []
        maxScore = 0
        for i in range(len(nums) + 1):
            score = zeroSum[i] + oneSum[i]
            if score > maxScore:
                maxScore = score
                res = [i]
            elif score == maxScore:
                res.append(i)
        return res