class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0] == '$' and sentence[i][1:].isnumeric(): 
                newPrice = format(int(sentence[i][1:]) * (100 - discount) / 100, '.2f')
                sentence[i] = '$' + str(newPrice)
        return ' '.join(sentence)
                