class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {order[i]: chr(ord('a') + i) for i in range(26)}
        return words == sorted(words, key = lambda x: [hashmap[i] for i in x])