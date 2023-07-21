class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # [length, count]

        memo = [[] for i in range(n)]

        def dp(index: int) -> list[int]:
            if memo[index]:
                return memo[index]

            length, count = 1, 1
            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    newLen, newCnt = dp(i)
                    if newLen > length - 1:
                        length, count = newLen + 1, newCnt
                    elif newLen == length - 1:
                        count += newCnt

            memo[index] = [length, count]
            return [length, count]

        for i in range(n):
            dp(i)

        maxLen, cnt = 0, 0
        for i in range(n):
            if memo[i][0] > maxLen:
                maxLen = memo[i][0]
                cnt = memo[i][1]
            elif memo[i][0] == maxLen:
                cnt += memo[i][1]
        return cnt
