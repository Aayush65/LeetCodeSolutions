class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        indexOf = lambda x: ord(x) - ord('a')
        
        freq1 = {indexOf(i): 0 for i in word1}
        for i in word1:
            freq1[indexOf(i)] += 1
        freq2 = {indexOf(i): 0 for i in word2}
        for i in word2:
            freq2[indexOf(i)] += 1
            
        def swap(i: int, j: int):
            i, j = indexOf(i), indexOf(j)
            if i not in freq2:
                freq2[i] = 0
            freq2[i] += 1
            if j not in freq1:
                freq1[j] = 0
            freq1[j] += 1
            
            freq1[i] -= 1
            if not freq1[i]:
                del freq1[i]
            freq2[j] -= 1
            if not freq2[j]:
                del freq2[j]
            
        for i in set(list(word1)):
            for j in set(list(word2)):
                swap(i, j)
                if len(freq1) == len(freq2):
                    return True
                swap(j, i)
        return False
        