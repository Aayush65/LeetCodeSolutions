class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        missing = {i for i in range(1, len(arr) + k + 1)}
        for i in arr:
            if i in missing:
                missing.remove(i)
        missing = sorted(list(missing))
        return missing[k - 1]