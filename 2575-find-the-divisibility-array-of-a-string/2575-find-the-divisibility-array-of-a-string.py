class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:        
        currNum = 0
        div = []
        for i in word:
            currNum = (currNum * 10 + int(i)) % m
            if currNum == 0:
                div.append(1)
            else:
                div.append(0)
        return div