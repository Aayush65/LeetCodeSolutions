class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        bloomMap = defaultdict(int)
        vals = set()
        for start, end in flowers:
            bloomMap[start] += 1
            bloomMap[end + 1] -= 1
            vals.add(start)
            vals.add(end + 1)

        vals = sorted(list(vals))
        total = 0
        for i in vals:
            total += bloomMap[i]
            bloomMap[i] = total
        # print(bloomMap, vals)

        ans = []
        for i in people:
            if i in bloomMap:
                ans.append(bloomMap[i])
                continue
            index = bisect_left(vals, i) - 1
            ans.append(0 if index == -1 else bloomMap[vals[index]])
        return ans