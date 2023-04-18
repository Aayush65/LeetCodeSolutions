class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = sorted(str(num), reverse=True)
        maxSwapNum = list(str(num))
        toBeSwapped = ''
        i = 0
        for i in range(len(numStr)):
            if maxSwapNum[i] != numStr[i]:
                toBeSwapped = maxSwapNum[i]
                maxSwapNum[i] = numStr[i]
                break
                
        if not toBeSwapped:
            return int(''.join(maxSwapNum))
        idxToBeSwapped = 0
        for j in range(i + 1, len(numStr)):
            if maxSwapNum[j] == maxSwapNum[i]:
                idxToBeSwapped = j
        maxSwapNum[idxToBeSwapped] = toBeSwapped
        return int(''.join(maxSwapNum))