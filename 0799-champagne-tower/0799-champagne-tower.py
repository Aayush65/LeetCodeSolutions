class Solution:
	def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

		dp = [[0]*x for x in range(1,102)]

		dp[0][0] = poured

		for row in range(query_row + 1):

			for col in range(row + 1):

				mid_pour = (dp[row][col] - 1.0) / 2.0

				if mid_pour > 0:

					dp[row+1][col] = dp[row+1][col] + mid_pour

					dp[row+1][col+1] = dp[row+1][col+1] + mid_pour

		result = min(1, dp[query_row][query_glass])

		return result