class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suffix = {i: 0 for i in nums}
        for i in nums:
            suffix[i] += 1
        prefix = set()
        res = []
        for i in nums:
            prefix.add(i)
            suffix[i] -= 1
            if suffix[i] == 0:
                del suffix[i]
            res.append(len(prefix) - len(suffix))
        return res