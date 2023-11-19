class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        for i in range(min(len(s1), len(s2), len(s3))):
            if s1[i] == s2[i] and s2[i] == s3[i]:
                i += 1
            else:
                break

        return len(s1) + len(s2) + len(s3) - 3 * i if i else -1