class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hm = defaultdict(int)
        for i in cpdomains:
            n, website = i.split()
            subs = deque(website.split('.'))
            while subs:
                hm['.'.join(subs)] += int(n)
                subs.popleft()
        
        res = []
        for i in hm:
            res.append(str(hm[i]) + " " + i)
        return res