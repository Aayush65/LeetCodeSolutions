class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        connected = {i: set() for i in nums}
        n = len(nums)
        MOD = int(1e9 + 7)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    connected[nums[i]].add(nums[j])
                    connected[nums[j]].add(nums[i])                

        indexs = {nums[i]: i for i in range(n)}

        @cache
        def backtrack(val: int, bitmask: int) -> int:
            if bitmask & 1 << indexs[val]:
                return 0
            res = 0
            bitmask |= 1 << indexs[val]
            if bitmask < 2 ** n - 1:
                for nei in connected[val]:
                    res += backtrack(nei, bitmask) % MOD
            else:
                res += 1
            bitmask ^= 1 << indexs[val]
            return res % MOD

        ans = 0
        for i in nums:
            ans += backtrack(i, 0)
        return ans % MOD
