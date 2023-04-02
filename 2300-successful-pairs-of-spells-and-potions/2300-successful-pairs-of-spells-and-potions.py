class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def search(target: int) -> int:
            i, j = 0, n
            while i < j:
                mid = (i + j) // 2
                if potions[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            return i
        
        potions.sort()
        pairs = []
        n = len(potions)
        for i in spells:
            pairs.append(n - search(success/i))
        return pairs