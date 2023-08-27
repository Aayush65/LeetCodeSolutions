class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r = 0
        l = 0
        other = 0
        for i in moves:
            if i == 'L':
                l += 1
            elif i == 'R':
                r += 1
            else:
                other += 1
        diff = abs(l - r)
        return diff + other