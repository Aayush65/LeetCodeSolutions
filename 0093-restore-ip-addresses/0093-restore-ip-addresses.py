class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        allIps = []

        def dfs(index: int, ip: list[int], dots) -> int:
            if dots == 0:
                return
            if index == len(s):
                if dots == 1:
                    allIps.append(''.join(ip))
                return
            if ip:
                ip.append('.')
            if s[index] == '0':
                ip.append('0')
                dfs(index + 1, ip, dots - 1)
                ip.pop()
                if ip:
                    ip.pop()
                return
            currNum = ''
            for i in range(index, min(len(s), index + 3)):
                currNum += s[i]
                if int(currNum) > 255:
                    break
                ip.append(currNum)
                dfs(i + 1, ip, dots - 1)
                ip.pop()
            if ip:
                ip.pop()

        dfs(0, [], 5)
        return allIps