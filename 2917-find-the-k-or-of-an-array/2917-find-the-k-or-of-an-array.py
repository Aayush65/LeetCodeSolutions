class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        kor = 0
        for i in range(32):
            count = 0
            for j in nums:
                if j & 2 ** i:
                    count += 1
                if count == k:
                    break
            if count == k:
                kor ^= 2 ** i
        return kor