class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        charMap = {chr(i + ord('a')): (i // 5, i % 5) for i in range(26)}

        @cache
        def findPath(start: str, end: str) -> str:
            q = deque([(charMap[start][0], charMap[start][1], [])])
            visited = set()
            while q:
                i, j, path = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                if board[i][j] == end:
                    return ''.join(path + ['!'])
                if i > 0:
                    q.append([i - 1, j, path + ['U']])
                if j > 0:
                    q.append([i, j - 1, path + ['L']])
                if i == 4 and j == 0:
                    q.append([5, 0, path + ['D']])
                if i < 4:
                    q.append([i + 1, j, path + ['D']])
                if j < 4 and i < 5:
                    q.append([i, j + 1, path + ['R']])

        mainPath = []
        prev = 'a'  
        for i in target:
            mainPath.append(findPath(prev, i))
            prev = i
        return ''.join(mainPath)