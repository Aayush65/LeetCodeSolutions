class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        q = [0]
        visited = set()
        farthest = 0
        while q:
            newQ = set()
            for index in q:
                if index == len(s) - 1:
                    return True
                if index in visited:
                    continue
                visited.add(index)
                for i in range(max(farthest + 1, minJump + index), min(len(s), maxJump + index + 1)):
                    farthest = max(i, farthest)
                    if i in visited or s[i] == '1':
                        continue
                    newQ.add(i)
            q = newQ
        return False