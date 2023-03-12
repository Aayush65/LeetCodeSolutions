class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hm = defaultdict(int)
        n = len(arr)
        for i in arr:
            hm[i] += 1

        arrSet = sorted(list(set(arr)), key = lambda x: -hm[x])
        count = 0
        setSize = 0
        for i in arrSet:
            count += hm[i]
            setSize += 1
            if count >= n / 2:
                break
        return setSize
        