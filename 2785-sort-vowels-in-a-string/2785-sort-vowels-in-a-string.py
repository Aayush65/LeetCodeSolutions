class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        res = []
        allVowels = []
        for i in s:
            if i in vowels:
                res.append('')
                allVowels.append(i)
            else:
                res.append(i)
        
        allVowels.sort()
        j = 0
        for i in range(len(s)):
            if not res[i]:
                res[i] = allVowels[j]
                j += 1
            
        return ''.join(res)