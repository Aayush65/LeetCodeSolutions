class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 1000000007
        nums.sort()
        
        subsequences = 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                subsequences += pow(2, j - i, mod)
                i += 1
        return subsequences % mod