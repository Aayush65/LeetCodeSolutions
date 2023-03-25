class Solution:
    def countCollisions(self, directions: str) -> int:
        newDirections = [[directions[0], 0]]
        for i in directions:
            if i == newDirections[-1][0]:
                newDirections[-1][1] += 1
            else:
                newDirections.append([i, 1])

        last = []
        count = 0
        for i, n in newDirections:
            if last and i != 'R':
                if i == 'S'and last[0] == 'R':
                    count += last[1]
                elif i == 'L':
                    if last[0] == 'R':
                        count += n + last[1]
                    else:
                        count += n
                last = ['S', 1]
            if i != 'L':
                last = [i, n]
        return count