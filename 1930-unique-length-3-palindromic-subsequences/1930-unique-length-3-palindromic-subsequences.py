class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = []
        curr = set()
        for i in s[::-1]:
            right.append(curr.copy())
            curr.add(i)
        
        palindromes = set()
        curr = set()
        for i in s:
            # print(curr, i, right[-1])
            for j in curr:
                if j in right[-1]:
                    palindromes.add(j + i)
            right.pop()
            curr.add(i)
        return len(palindromes)