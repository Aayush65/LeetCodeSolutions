class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        for i in range(23, -1, -1):
            a, b = [int(j) for j in str(i).zfill(2)]
            if a in arr:
                arr.remove(a)
                if b in arr:
                    arr.remove(b)
                    min1 = arr[0] * 10 + arr[1]
                    min2 = arr[1] * 10 + arr[0]
                    if max(min1, min2) < 60:
                        return f"{a}{b}:{str(max(min1, min2)).zfill(2)}"
                    if min(min1, min2) < 60:
                        return f"{a}{b}:{str(min(min1, min2)).zfill(2)}"
                    arr.append(b)
                arr.append(a)
        return ""