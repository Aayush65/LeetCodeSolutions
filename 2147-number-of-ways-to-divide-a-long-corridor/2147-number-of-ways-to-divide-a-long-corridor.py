class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(index: int) -> int:
            if index == len(corridor):
                return 0
            seats = 0
            ways = 0
            plants = 1
            for i in range(index, len(corridor)):
                if corridor[i] == 'S':
                    seats += 1
                    if seats == 2:
                        ways += 1
                if corridor[i] == 'P' and seats == 2:
                    plants += 1
                if seats == 3:
                    return (plants * dp(i)) % mod
            return ways % mod

        return dp(0)