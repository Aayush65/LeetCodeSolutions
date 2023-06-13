class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        def dp(index: int, prev: int) -> int:
            if index == len(arr):
                return 0
            visited.add(index)
            nextIdx = bisect_left(arr, arr[index] + prev, lo = index + 1)
            if nextIdx < len(arr) and arr[nextIdx] == prev + arr[index]:
                return 1 + dp(nextIdx, arr[index])
            return 1
        
        maxLen = 1
        visited = set()
        for i in range(len(arr)):
            # if i in visited:
            #     continue
            for j in range(i + 1, len(arr)):
                maxLen = max(maxLen, 1 + dp(j, arr[i]))
        return maxLen if maxLen > 2 else 0