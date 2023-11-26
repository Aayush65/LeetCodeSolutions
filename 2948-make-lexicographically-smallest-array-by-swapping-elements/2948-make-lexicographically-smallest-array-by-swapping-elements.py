class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted([(x, i) for i, x in enumerate(nums)])

        realIdx = {i: [] for i in nums}

        divs = []
        curr = []
        for x, i in sorted_nums:
            if not curr or x - curr[-1][0] <= limit:
                curr.append((x, i))
            else:
                if len(curr) > 1:
                    divs.append(curr)
                curr = [(x, i)]
        if len(curr) > 1:
            divs.append(curr)

        for div in divs:
            indices = sorted([i[1] for i in div])
            div.sort()
            for idx, val in zip(indices, div):
                realIdx[val[0]].append(idx)                

        for val in realIdx:
            for i in realIdx[val]:
                nums[i] = val
        return nums