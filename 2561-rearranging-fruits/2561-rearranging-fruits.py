class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1, freq2 = Counter(basket1), Counter(basket2)
        extra1, extra2 = [], []
        mini = min(min(basket1), min(basket2))

        for i in freq1:
            diff = freq1[i] - freq2[i]
            if diff % 2:
                return -1
            if diff:
                for _ in range(diff // 2): extra1.append(i)
        
        for i in freq2:
            diff = freq2[i] - freq1[i]
            if diff % 2:
                return -1
            if diff:
                for _ in range(diff // 2): extra2.append(i)
        
        if len(extra1) != len(extra2): return -1
        extra1.sort()
        extra2.sort()
        cost = 0
        for i in extra1:
            cost += min(i, extra2.pop(), mini * 2)
        return cost