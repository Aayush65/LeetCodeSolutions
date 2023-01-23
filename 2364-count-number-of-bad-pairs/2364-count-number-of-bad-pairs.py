class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        n = len(nums)
        goodPairs = 0
        for i in range(n):
            diff = i - nums[i]
            goodPairs += hashmap[diff]
            hashmap[diff] += 1
        return n * (n - 1) // 2 - goodPairs