class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward = sorted([[reward1[i], reward2[i]] for i in range(len(reward1))], key = lambda x: x[1] - x[0])
        total = 0
        for i in range(k):
            total += reward[i][0]
        for i in range(k, len(reward)):
            total += reward[i][1]
        return total