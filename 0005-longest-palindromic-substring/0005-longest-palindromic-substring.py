class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        longestSubstr = ''
        subStr = [-1, -1]
        subLength = 0
        while i < len(s):
            j = i + 1

            # even substrings
            tempi, tempj = i , j
            length = 0
            while tempi > -1 and tempj < len(s) and s[tempi] == s[tempj]:
                length += 2
                tempi -= 1
                tempj += 1
            if length > subLength:
                subLength = length
                subStr = [tempi + 1, tempj]

            # odd substrings
            tempi, tempj = i - 1, j
            length = 1
            while tempi > -1 and tempj < len(s) and s[tempi] == s[tempj]:
                length += 2
                tempi -= 1
                tempj += 1
            if length > subLength:
                subLength = length
                subStr = [tempi + 1, tempj]
            i += 1

        for i in range(subStr[0], subStr[1]):
            longestSubstr += s[i]
        return longestSubstr
