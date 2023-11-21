class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        score = lambda x: x - int(str(x)[::-1])
        
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[score(i)] += 1
        
        mod = int(1e9 + 7)
        count = 0
        for i in nums:
            hashmap[score(i)] -= 1
            count += hashmap[score(i)]
            count %= mod
        return count