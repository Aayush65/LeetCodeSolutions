class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 33
        for i in nums:
            for j in range(32):
                if abs(i) & 2 ** j:
                    bits[j] += 1
            if i < 0:
                bits[32] += 1
        ans = 0
        for i in range(32):
            if bits[i] % 3:
                ans += 2 ** i
        if bits[32] % 3:
            ans = -ans
        return ans