class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        stack = []
        res = []
        for i in range(1, n + 1):
            stack.append(i)
            res.append("Push")
            if stack[-1] == target[j]:
                j += 1
            else:
                stack.pop()
                res.append("Pop")
            if j == len(target):
                break
        return res