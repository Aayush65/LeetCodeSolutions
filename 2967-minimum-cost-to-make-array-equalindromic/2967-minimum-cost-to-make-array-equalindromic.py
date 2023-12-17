class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        def calcCost(palindrome: int) -> int:
            cost = 0
            for i in nums:
                cost += abs(palindrome - i)
            return cost
        
        def findPalindrome(num: int, inc: int) -> int:
            while str(num) != str(num)[::-1]:
                num += inc
            return num
        
        if n % 2:
            mid = nums[n // 2]
            inc = calcCost(findPalindrome(mid, 1))
            dec = calcCost(findPalindrome(mid, -1))
            return min(inc, dec)
        
        mid = nums[n // 2 - 1] + nums[n // 2]
        if mid % 2 == 0:
            mid //= 2
            inc = calcCost(findPalindrome(mid, 1))
            dec = calcCost(findPalindrome(mid, -1))
            return min(inc, dec)
        
        mid1 = mid // 2
        mid2 = mid // 2 + 1
        inc1 = calcCost(findPalindrome(mid1, 1))
        dec1 = calcCost(findPalindrome(mid1, -1))
        inc2 = calcCost(findPalindrome(mid2, 1))
        dec2 = calcCost(findPalindrome(mid2, -1))
        return min(inc1, dec1, inc2, dec2)
        