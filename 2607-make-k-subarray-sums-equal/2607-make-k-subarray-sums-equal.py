class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        ops = 0
        k = gcd(len(arr), k)
        for i in range(k):
            medianArr = sorted([arr[j] for j in range(i, len(arr), k)])
            median = medianArr[len(medianArr) // 2]
            ops += sum(abs(j- median) for j in medianArr)
        return ops
