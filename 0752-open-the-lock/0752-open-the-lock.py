class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        toStr = lambda x: ''.join([str(i) for i in x])

        q = {'0000'}
        visited = set()
        steps = 0
        while q:
            newQ = set()
            for i in q:
                if i == target:
                    return steps
                if i in visited or i in deadends:
                    continue
                visited.add(i)
                comb = [int(j) for j in i]
                for k in range(4):
                    comb[k] = (comb[k] + 1) % 10
                    newQ.add(toStr(comb))
                    comb[k] = (comb[k] - 2) % 10
                    newQ.add(toStr(comb))
                    comb[k] = (comb[k] + 1) % 10
            steps += 1
            q = newQ
        return -1