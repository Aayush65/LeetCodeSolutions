class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        hm = {chars[i]: i for i in range(len(chars))}
        indexOf = lambda x: ord(x) - ord('a') + 1
        
        arr = []
        for i in s:
            if i in hm:
                arr.append(vals[hm[i]])
            else:
                arr.append(indexOf(i))
        
        maxSum = 0
        currTotal = 0
        for i in arr:
            currTotal += i
            if currTotal < 0:
                currTotal = 0
            maxSum = max(maxSum, currTotal)
        return maxSum