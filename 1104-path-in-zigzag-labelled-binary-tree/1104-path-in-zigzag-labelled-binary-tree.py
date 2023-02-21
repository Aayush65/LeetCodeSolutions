class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = [label]
        while label > 1:
            level = int(log2(label))
            label = 2 ** (level - 1) + 2 ** level - label // 2 - 1
            path.append(label)
        return path[::-1]