class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sumCount = defaultdict(int)
        sumCount[0] = 1
        total = 0
        for i in nums:
            total += i
            count += sumCount[total - goal]
            sumCount[total] += 1
        return count