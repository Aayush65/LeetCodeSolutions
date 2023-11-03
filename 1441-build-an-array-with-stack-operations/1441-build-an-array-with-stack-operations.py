class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        res = []
        for i in range(1, n + 1):
            res.append("Push")
            if i == target[j]:
                j += 1
            else:
                res.append("Pop")
            if j == len(target):
                break
        return res