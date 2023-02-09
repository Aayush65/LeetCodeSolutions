class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        prefixMap = defaultdict(set)
        for idea in ideas:
            prefixMap[idea[0]].add(idea[1:])

        total = 0
        for firstSet in prefixMap:
            for secondSet in prefixMap:
                if firstSet == secondSet:
                    continue
                count = 0
                for i in prefixMap[secondSet]:
                    if i in prefixMap[firstSet]:
                        count += 1
                total += (len(prefixMap[secondSet]) - count) * (len(prefixMap[firstSet]) - count)

        return total