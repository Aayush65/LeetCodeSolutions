class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        hashset = set()
        arrSet = set(arr)
        for i in arrSet:
            hashset.add(hashmap[i])
        
        return len(arrSet) == len(hashset)
