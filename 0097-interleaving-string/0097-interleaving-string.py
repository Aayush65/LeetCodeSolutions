class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        failed = set()

        def dp(i: int, j: int) -> bool:
            if i + j == len(s3):
                return True
            if (i, j) in failed:
                return False
            if i < len(s1) and s1[i] == s3[i + j]:
                if dp(i + 1, j):
                    return True
            if j < len(s2) and s2[j] == s3[i + j]:
                if dp(i, j + 1):
                    return True
            failed.add((i, j))
            return False

        return dp(0, 0)