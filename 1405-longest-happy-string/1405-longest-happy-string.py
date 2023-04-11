class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = []
        H = []
        if a:
            heappush(H, [-a, 'a'])
        if b:
            heappush(H, [-b, 'b'])
        if c:
            heappush(H, [-c, 'c'])
        while H:
            count, char = heappop(H)
            sameAsPrev = []
            if s and s[-1][0] == char:
                sameAsPrev = [count, char]
                if H:
                    count, char = heappop(H)
                else:
                    break
            bigExists = len(sameAsPrev) != 0
            if -count > 2 and not bigExists:
                s.append(char * 2)
                heappush(H, [count + 2, char])
            else:
                if bigExists:
                    s.append(char)
                    if count != -1:
                        heappush(H, [count + 1, char])
                else:
                    s.append(char * -count)
            if sameAsPrev:
                heappush(H, sameAsPrev)
        return ''.join(s)