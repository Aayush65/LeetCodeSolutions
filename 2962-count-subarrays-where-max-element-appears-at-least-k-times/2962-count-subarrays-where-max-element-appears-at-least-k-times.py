class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        freq = [0]
        for i in nums:
            if i == maxi:
                freq.append(freq[-1] + 1)
            else:
                freq.append(freq[-1])
        
        n = len(nums)
        res = 0
        for i in range(n):
            end = bisect_left(freq, k + freq[i])
            if end == n + 1:
                break
            res += n - end + 1
        return res