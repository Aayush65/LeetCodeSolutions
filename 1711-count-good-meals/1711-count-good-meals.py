class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = []
        for i in range(ceil(log2(2 * max(deliciousness))), -1, -1):
            powers.append(1 << i)

        eleMap = {i: 0 for i in deliciousness}
        for i in deliciousness:
            eleMap[i] += 1
        
        pairs = 0
        for i in eleMap:
            if not i:
                continue
            for j in powers:
                if i > j:
                    break
                if j == 2 * i:
                    pairs += eleMap[i] * (eleMap[i] - 1) // 2
                    if 0 in eleMap:
                        pairs += eleMap[i] * eleMap[0]
                elif j - i in eleMap and i != j:
                    pairs += eleMap[i] * eleMap[j - i]
            eleMap[i] = 0
        return pairs % 1000000007