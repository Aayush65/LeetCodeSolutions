class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        extraRungs = ceil((rungs[0]) / dist) - 1
        for i in range(1, len(rungs)):
            extraRungs += ceil((rungs[i] - rungs[i - 1]) / dist) - 1
        return extraRungs