class Solution:
    def partition(self, s: str) -> List[List[str]]:
        allPalindromes = []
    
        def isPalindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtracking(index: int, palindromes: list[str]) -> None:
            if index == len(s):
                nonlocal allPalindromes
                allPalindromes.append(palindromes.copy())
                return
            # currStr = ''
            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    palindromes.append(s[index : i + 1])
                    backtracking(i + 1, palindromes)
                    palindromes.pop()

        backtracking(0, [])
        return allPalindromes