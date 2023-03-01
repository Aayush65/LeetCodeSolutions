class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(i: int, j: int) -> list[int]:
            if j - i == 0:
                return [nums[i]]
            left = mergeSort(i, (i + j) // 2)
            right = mergeSort((i + j) // 2 + 1, j)
            res = []
            i, j = 0, 0
            while len(res) < len(left) + len(right):
                if i >= len(left) or (j < len(right) and left[i] >= right[j]):
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            return res

        return mergeSort(0, len(nums) - 1)