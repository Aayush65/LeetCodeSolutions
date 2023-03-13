class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        res = []
        for i in nums:
            if hm[i] > 1 or hm[i + 1] or hm[i - 1]:
                continue
            res.append(i)
        return res
            