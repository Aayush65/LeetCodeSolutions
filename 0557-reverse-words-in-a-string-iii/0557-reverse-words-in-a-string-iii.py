class Solution:
    def reverseWords(self, s: str) -> str:
        reversedString = ''
        i = 0
        while i < len(s):
            word = ''
            while i < len(s) and s[i] != ' ':
                word = s[i] + word
                i += 1
            if i < len(s):
                reversedString += word + s[i]
            else:
                reversedString += word
            i += 1
        return reversedString           