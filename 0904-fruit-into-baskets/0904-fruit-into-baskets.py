class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i, j = 0, 1
        hashmap = {fruits[i]: 1}
        while j < n and len(hashmap) < 3:
            if fruits[j] not in hashmap:
                hashmap[fruits[j]] = 0
            hashmap[fruits[j]] += 1
            j += 1
        if len(hashmap) == 3:
            j -= 1      
            del hashmap[fruits[j]] 

        maxLen = j - i
        while j < n:
            maxLen = max(maxLen, j - i)
            while i < j and len(hashmap) > 1:
                hashmap[fruits[i]] -= 1
                if not hashmap[fruits[i]]:
                    del hashmap[fruits[i]]
                i += 1

            while j < n and len(hashmap) < 3:
                if fruits[j] not in hashmap:
                    hashmap[fruits[j]] = 0
                hashmap[fruits[j]] += 1
                j += 1
            if len(hashmap) == 3:
                j -= 1      
                del hashmap[fruits[j]] 

        maxLen = max(maxLen, j - i)
        return maxLen