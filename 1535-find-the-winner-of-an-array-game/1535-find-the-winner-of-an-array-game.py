class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxVal = max(arr)
        arr = deque(arr)
        curr, orgK = arr[0], k
        while k and arr[0] != maxVal:
            a = arr.popleft()
            b = arr.popleft()
            maxi, mini = max(a, b), min(a, b)
            arr.appendleft(maxi)
            arr.append(mini)
            if arr[0] != curr:
                curr = arr[0]
                k = orgK
            k -= 1
        return arr[0]