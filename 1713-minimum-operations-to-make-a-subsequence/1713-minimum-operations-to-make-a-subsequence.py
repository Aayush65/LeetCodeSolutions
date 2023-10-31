class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        
        indexMap = {target[i]: i for i in range(len(target))}
        arr = [indexMap[i] for i in arr if i in indexMap]
    
        lis = []
        for i in arr:
            if not lis or lis[-1] < i:
                lis.append(i)
            else:
                index = bisect_left(lis, i)
                lis[index] = i

        return len(target) - len(lis)