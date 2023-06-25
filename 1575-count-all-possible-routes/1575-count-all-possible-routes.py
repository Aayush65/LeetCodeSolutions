class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(index: int, fuel: int) -> int:
            if fuel < 0:
                return 0
            res = 1 if index == finish else 0
            for i in range(len(locations)):
                if i ==  index:
                    continue
                res = (res + dp(i, fuel - abs(locations[i] - locations[index]))) % mod
            return res            
            
        return dp(start, fuel)