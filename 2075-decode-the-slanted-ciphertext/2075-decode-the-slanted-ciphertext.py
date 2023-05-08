class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        res = []
        cols = len(encodedText) // rows
        for i in range(cols):
            for j in range(rows):
                if i + j * cols + j >= len(encodedText):
                    break
                res.append(encodedText[i + j * cols + j])
        while res and res[-1] == ' ':
            res.pop()
        return ''.join(res)