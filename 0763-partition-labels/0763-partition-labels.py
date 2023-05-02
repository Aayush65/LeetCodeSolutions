class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqMap = [0] * 26
        indexOf = lambda x: ord(x) - ord('a')
        for i in s:
            freqMap[indexOf(i)] += 1
        
        chars = [0] * 26
        sets = []
        for i in s:
            chars[indexOf(i)] += 1
            freqMap[indexOf(i)] -= 1
                
            isDisjoint = True
            for i in range(26):
                if chars[i] and freqMap[i]:
                    isDisjoint = False
                    break
            if isDisjoint:
                sets.append(sum(chars))
                chars = [0] * 26
        return sets