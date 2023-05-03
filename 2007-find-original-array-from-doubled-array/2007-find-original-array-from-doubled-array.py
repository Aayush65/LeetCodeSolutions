class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        eleMap = defaultdict(int)
        for i in changed:
            eleMap[i] += 1
        changed.sort()
        
        org = []
        zeroes = 0
        for i in changed:
            if i and eleMap[i]:
                if eleMap[i * 2]:
                    org.append(i)
                    eleMap[i * 2] -= 1
                    eleMap[i] -= 1
                else:
                    return []
            if not i:
                zeroes += 1
        if zeroes % 2:
            return []
        for i in range(zeroes // 2):
            org.append(0)
        return org