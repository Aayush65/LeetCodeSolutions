class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while i < len(chars):
            chars[j] = chars[i]
            j += 1
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            if count > 1:
                for digits in str(count):
                    chars[j] = digits
                    j += 1
            i += 1
        return j