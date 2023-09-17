class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def countBits(x: int) -> int:
            count = 0
            while x:
                if x % 2:
                    count += 1
                x //= 2
            return count
        
        count = 0
        for i in range(len(nums)):
            if countBits(i) == k:
                count += nums[i]
        return count