class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = {i: 0 for i in nums}
        for i in nums:
            freq[i] += 1

        nums = [(i, freq[i]) for i in sorted(freq.keys(), reverse = True)]
        ops, prev = 0, 0
        for i, count in nums:
            if i == nums[-1][0]:
                break
            prev += count
            ops += prev
        return ops