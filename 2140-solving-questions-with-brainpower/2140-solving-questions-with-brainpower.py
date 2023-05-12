class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(index: int) -> int:
            if index >= len(questions):
                return 0
            return max(dp(index + 1), dp(index + questions[index][1] + 1) + questions[index][0])
        
        return dp(0)