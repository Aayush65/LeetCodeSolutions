class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)
        finalFreq = Counter(nums)
        breaks = -1
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
            if freq[i] == finalFreq[i]:
                del freq[i]
            breaks += len(freq) == 0
        
        res = pow(2, breaks, mod)
        return res