class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = deque(sentence1.split())
        s2 = deque(sentence2.split())
        
        if len(s2) > len(s1):
            s1, s2 = s2, s1
            
        while s2:
            if s1[0] != s2[0]:
                break
            else:
                s1.popleft()
                s2.popleft()
        
        while s2:
            if s1[-1] != s2[-1]:
                break
            else:
                s1.pop()
                s2.pop()
        
        return not s2