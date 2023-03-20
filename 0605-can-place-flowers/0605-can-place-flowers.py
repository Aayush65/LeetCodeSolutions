class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                continue
            if (i > 0 and flowerbed[i - 1]) or (i < len(flowerbed) - 1 and flowerbed[i + 1]):
                continue
            flowerbed[i] = 1
            n -= 1
        return n <= 0