class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refilled = 0
        n = len(plants)
        i, j = 0, n - 1
        water1, water2 = capacityA, capacityB
        while i <= j:
            if i == j:
                if water1 >= water2:
                    if water1 < plants[i]:
                        refilled += 1
                    i += 1
                else:
                    if water2 < plants[j]:
                        refilled += 1
                    j -= 1
            else:
                if water1 < plants[i]:
                    refilled += 1
                    water1 = capacityA
                water1 -= plants[i]
                i += 1
                if water2 < plants[j]:
                    refilled += 1
                    water2 = capacityB
                water2 -= plants[j]
                j -= 1
        return refilled