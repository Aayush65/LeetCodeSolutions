class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hm = {i: 0 for i in arr}
        for i in arr:
            hm[i] += 1
        
        arr = [[hm[i], i] for i in hm]
        arr.sort()
        count = 0
        for i, j in arr:
            if k:
                if k >= i:
                    k -= i
                else:
                    k = 0
                    count += 1
            else:
                count += 1
        return count