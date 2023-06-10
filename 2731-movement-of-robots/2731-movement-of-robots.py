class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 1000000007
        for i in range(len(s)):
            if s[i] == "L":
                nums[i] -= d;
            else:
                nums[i] += d;
        
        nums.sort()
        total = 0
        ans = 0
        for i in range(len(nums)):
            ans += nums[i] * i - total
            ans %= mod
            total += nums[i]
        return ans