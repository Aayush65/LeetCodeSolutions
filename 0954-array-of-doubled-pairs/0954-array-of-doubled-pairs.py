class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key = lambda x: [abs(x), x])
        eleMap = defaultdict(int)
        for i in arr:
            eleMap[i] += 1
        
        zeroes = 0
        for i in arr:
            if i and eleMap[i]:
                if eleMap[i * 2]:
                    eleMap[i * 2] -= 1
                    eleMap[i] -= 1
                else:
                    return False
            if not i:
                zeroes += 1
        return zeroes % 2 == 0