class TextEditor:

    def __init__(self):
        self.leftText = []
        self.rightText = []
        self.cursor = 0

    def addText(self, text: str) -> None:
        for i in text:
            self.leftText.append(i)
            self.cursor += 1

    def deleteText(self, k: int) -> int:
        deleted = 0
        for i in range(min(k, self.cursor)):
            self.leftText.pop()
            self.cursor -= 1
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        for i in range(min(k, len(self.leftText))):
            self.rightText.append(self.leftText.pop())
            self.cursor -= 1
        return self.last10Chars()
            
    def cursorRight(self, k: int) -> str:
        for i in range(min(k, len(self.rightText))):
            self.leftText.append(self.rightText.pop())
            self.cursor += 1
        return self.last10Chars()
    
    def last10Chars(self) -> str:
        res = []
        for i in range(min(10, len(self.leftText))):
            res.append(self.leftText[-1 - i])
        res.reverse()
        return ''.join(res)

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)