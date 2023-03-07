class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 1
        res = 0
        for i in nums:
            if j == i:
                j += 1
            elif j < i:
                if i - j > k:
                    res += k * (j + j + k - 1) // 2
                    k = 0
                    j += k
                    break
                k -= i - j
                res += ((i - j) * (j + i - 1)) // 2
                j = i + 1
        if k > 0:
            res += (k * (j + j + k - 1)) // 2
        return res
