class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXOR = [0]
        for i in arr:
            preXOR.append(preXOR[-1] ^ i)

        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if preXOR[i] == preXOR[j + 1]:
                    count += j - i
        return count