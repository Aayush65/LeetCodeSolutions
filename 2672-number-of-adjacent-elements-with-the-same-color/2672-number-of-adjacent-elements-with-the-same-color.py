class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        currAdjPairs = 0
        nums = [0] * n
        res = []
        for i, color in queries:
            if i > 0 and nums[i] == nums[i - 1] and nums[i]:
                currAdjPairs -= 1
            if i < n - 1 and nums[i] == nums[i + 1] and nums[i]:
                currAdjPairs -= 1
            nums[i] = color
            if i > 0 and nums[i] == nums[i - 1] and nums[i]:
                currAdjPairs += 1
            if i < n - 1 and nums[i] == nums[i + 1] and nums[i]:
                currAdjPairs += 1
            res.append(currAdjPairs)
        return res