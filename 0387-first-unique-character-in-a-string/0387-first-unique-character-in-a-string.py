class Solution:
    def firstUniqChar(self, s: str) -> int:
        pos = {}
        for i, x in enumerate(s):
            if x in pos:
                pos[x] = float("inf")
            else:
                pos[x] = i
        res = min(pos.values())
        return res if res != float("inf") else -1
