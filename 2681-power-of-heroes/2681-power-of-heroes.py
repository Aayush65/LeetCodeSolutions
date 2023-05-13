class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        mod = 1000000007
        power = 0
        pre = 0
        for i in nums:
            power += i ** 3 + i * i * pre
            power %= mod
            pre = pre * 2 + i
        return power