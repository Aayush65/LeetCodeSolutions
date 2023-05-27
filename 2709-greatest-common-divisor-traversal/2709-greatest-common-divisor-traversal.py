class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if 1 in nums and len(nums) != 1:
            return False
        nums = set(nums)
        nums = list(nums)
        
        factors = set()
        def findFactors(n: int) -> set[int]:
            primeFactors = []
            if n % 2== 0:
                primeFactors.append(2)
            while n % 2 == 0:
                n = n // 2
            for i in range(3,int(math.sqrt(n))+1,2):
                if n % i == 0:
                    primeFactors.append(i)                    
                while n % i== 0:
                    n = n // i
            if n > 2:
                primeFactors.append(n)
            for i in primeFactors:
                factors.add(i)
            return primeFactors
            
        factorList = []
        for i in nums:
            factorList.append(findFactors(i))
        
        par = {i: i for i in factors}
        rank = {i: 1 for i in factors}            
        
        def find(n: int) -> int:
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1: int, n2: int) -> None:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0
            return True  
        
        for i in factorList:
            for j in range(1, len(i)):
                union(i[j - 1], i[j])
        
        flag = 2
        for i in rank:
            if rank[i]:
                flag -= 1
            if not flag:
                return False
        return True