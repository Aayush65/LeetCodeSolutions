class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        final = [[1,2,3],[4,5,0]]
        q = deque([board])
        steps = 0
        visited = set()
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == final:
                    return steps
                if tuple(curr[0] + curr[1]) in visited:
                    continue
                visited.add(tuple(curr[0] + curr[1]))

                zi, zy = -1, -1
                for i in range(2):
                    for j in range(3):
                        if not curr[i][j]:
                            zi, zy = i, j

                if zi == 0:
                    curr[zi][zy], curr[zi + 1][zy] = curr[zi + 1][zy], curr[zi][zy]
                    q.append([i.copy() for i in curr])
                    curr[zi][zy], curr[zi + 1][zy] = curr[zi + 1][zy], curr[zi][zy]
                if zi == 1:
                    curr[zi][zy], curr[zi - 1][zy] = curr[zi - 1][zy], curr[zi][zy]
                    q.append([i.copy() for i in curr])
                    curr[zi][zy], curr[zi - 1][zy] = curr[zi - 1][zy], curr[zi][zy]
                if zy > 0:
                    curr[zi][zy], curr[zi][zy - 1] = curr[zi][zy - 1], curr[zi][zy]
                    q.append([i.copy() for i in curr])
                    curr[zi][zy], curr[zi][zy - 1] = curr[zi][zy - 1], curr[zi][zy]
                if zy < 2:
                    curr[zi][zy], curr[zi][zy + 1] = curr[zi][zy + 1], curr[zi][zy]
                    q.append([i.copy() for i in curr])
                    curr[zi][zy], curr[zi][zy + 1] = curr[zi][zy + 1], curr[zi][zy]
            steps += 1
        return -1