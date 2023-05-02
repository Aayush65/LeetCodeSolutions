class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        
        for num in sorted(hm):
            if not hm[num]:
                continue
            for i in range(1, k):
                if hm[i + num] >= hm[num]:
                    hm[i + num] -= hm[num]
                else:
                    return False
            hm[num] = 0
        return True