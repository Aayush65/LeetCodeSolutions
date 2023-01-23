class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        allIps = []

        def dfs(index: int, ip: list[int], dots) -> int:
            if index == len(s):
                if dots == 4:
                    allIps.append(''.join(ip[:-1]))
                return
            if dots > 3:
                return
            if s[index] == '0':
                ip.append('0')
                dfs(index + 1, ip + ['.'], dots + 1)
                ip.pop()
                return
            currNum = ''
            for i in range(index, min(len(s), index + 3)):
                currNum += s[i]
                if int(currNum) > 255:
                    break
                ip.append(currNum)
                dfs(i + 1, ip + ['.'], dots + 1)
                ip.pop()

        dfs(0, [], 0)
        return allIps