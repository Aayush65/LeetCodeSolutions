class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] % k:
                continue
            hcf = nums[i]
            for j in range(i, len(nums)):
                hcf = gcd(nums[j], hcf)
                if hcf < k:
                    break
                if hcf == k:
                    count += 1
        return count