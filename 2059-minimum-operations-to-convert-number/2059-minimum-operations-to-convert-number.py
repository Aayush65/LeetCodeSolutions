class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = {start}
        steps = 0
        visited = set()
        while q:
            newQ = set()
            for i in q:
                if i == goal:
                    return steps
                if i in visited or i < 0 or i > 1000:
                    continue
                visited.add(i)
                for num in nums:
                    newQ.add(i + num)
                    newQ.add(i - num)
                    newQ.add(i ^ num)
            q = newQ
            steps += 1
        return -1                    