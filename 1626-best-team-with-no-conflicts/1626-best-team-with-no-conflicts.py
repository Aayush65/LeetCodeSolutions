class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        team = [[ages[i], scores[i]] for i in range(n)]
        team.sort()
        
        dp = [i[1] for i in team]
        for i in range(n - 2, -1, -1):
            prevScore = 0
            for j in range(n - 1, i, -1):
                if team[i][0] == team[j][0] or team[i][1] <= team[j][1]:
                    prevScore = max(prevScore, dp[j])
            dp[i] += prevScore

        return max(dp)
        
        