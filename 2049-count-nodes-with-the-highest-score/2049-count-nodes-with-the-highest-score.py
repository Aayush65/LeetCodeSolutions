class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for i in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        
        subTreeLen = [[0, 0] for i in range(n)]

        def findSubtreeLen(node: int) -> int:
            if children[node]:
                subTreeLen[node][0] = 1 + findSubtreeLen(children[node][0])
            if len(children[node]) == 2:
                subTreeLen[node][1] = 1 + findSubtreeLen(children[node][1])
            return sum(subTreeLen[node])

        findSubtreeLen(0)
        highestScore = 1
        res = 0
        erase = lambda x: x if x else 1
        for i in range(n):
            up = n - sum(subTreeLen[i]) - 1
            left, right = subTreeLen[i]
            up = erase(up)
            left = erase(left)
            right = erase(right)
            score = up * left * right
            if score > highestScore:
                highestScore = score 
                res = 0
            if score == highestScore:
                res += 1
        return res


