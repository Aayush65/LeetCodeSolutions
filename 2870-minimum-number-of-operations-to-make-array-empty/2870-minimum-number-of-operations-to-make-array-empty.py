class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freqs = Counter(nums).values()
        count = 0
        for i in freqs:
            if i < 2:
                return -1
            if i % 3:
                count += 1
            count += i // 3
        return count
    