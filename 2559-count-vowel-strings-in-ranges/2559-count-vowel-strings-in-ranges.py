class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        isSatisfy = []
        for i in words:
            isSatisfy.append(i[0] in vowels and i[-1] in vowels)
        prefixSum = [0]
        for i in isSatisfy:
            prefixSum.append(prefixSum[-1] + 1 if i else prefixSum[-1])
        
        res = []
        for i, j in queries:
            res.append(prefixSum[j + 1] - prefixSum[i])
        return res
            
            