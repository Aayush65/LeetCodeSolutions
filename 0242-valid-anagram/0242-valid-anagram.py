class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(list(s)) == Counter(list(t))