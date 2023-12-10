class Solution:
    def countTestedDevices(self, battery: List[int]) -> int:
        count = 0
        for i in battery:
            i -= count
            if i > 0:
                count += 1
        return count