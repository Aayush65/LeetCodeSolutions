class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # hashset = {ord(i) - ord('a') for i in letters}
        # for i in range(ord(target) - ord('a') + 1, 26):
        #     print(chr(i + ord('a')))
        #     if i in hashset:
        #         return chr(i + ord('a'))
        # return letters[0]
    
        res = '0'
        for i in letters:
            if i > target and (res == '0' or i < res):
                res = i
        return res if res != '0' else letters[0]