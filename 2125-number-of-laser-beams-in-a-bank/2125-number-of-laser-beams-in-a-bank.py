class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [[int(j) for j in i] for i in bank]
        security = [sum(i) for i in bank if sum(i)]
        total = 0
        for i in range(1, len(security)):
            total += security[i] * security[i - 1]
        return total