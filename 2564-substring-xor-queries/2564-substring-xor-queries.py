class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        lengths = set()
        for first, second in queries:
            lengths.add(len(bin(first ^ second)) - 2)
        
        numMap = {}
        for length in lengths:
            for i in range(len(s) - length + 1):
                if s[i] == '0':
                    if 0 not in numMap:
                        numMap[0] = [i, i]
                    continue
                newNum = int(s[i: i + length], 2)
                if newNum not in numMap:
                    numMap[newNum] = [i, i + length - 1]
        
        res = []
        for first, second in queries:
            num = first ^ second
            if num in numMap:
                res.append(numMap[num])
            else:
                res.append([-1,-1])
        return res