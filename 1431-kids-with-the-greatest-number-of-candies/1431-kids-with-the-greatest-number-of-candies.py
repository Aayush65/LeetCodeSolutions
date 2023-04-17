class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = candies[0]
        for i in candies:
            if i > maxi:
                maxi = i
        return [i + extraCandies >= maxi for i in candies]