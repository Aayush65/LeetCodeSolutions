class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q = {(0, True)}
        visited = set()
        steps = 0
        while q:
            newQ = set()
            for i, canGoBack in q:
                if i == x:
                    return steps
                if (i, canGoBack) in visited or i in forbidden or i > max(x, max(forbidden)) + a + b:
                    continue
                visited.add((i, canGoBack))
                newQ.add((i + a, True))
                if canGoBack and i - b >= 0:
                    newQ.add((i - b, False))                
            steps += 1
            q = newQ
        return -1