class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1: str, n2: str) -> int:
            if n1 + n2 >= n2 + n1:
                return -1
            else:
                return 1
        
        nums = list(map(str, nums))
        nums.sort(key = cmp_to_key(compare))
        # print(nums)
        return str(int(''.join(nums)))