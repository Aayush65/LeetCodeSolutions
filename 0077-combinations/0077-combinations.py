class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allCombs = []
    
        def combinations(i: int, arr: list[int]) -> None:
            if len(arr) == k:
                allCombs.append(arr.copy())
            if i > n:
                return
            for j in range(i + 1, n + 1):
                arr.append(j)
                combinations(j , arr)
                arr.pop()

        combinations(0, [])
        return allCombs