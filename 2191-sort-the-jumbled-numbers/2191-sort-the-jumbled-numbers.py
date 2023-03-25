class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped(num: int) -> int:
            n = []
            for i in str(num):
                n.append(str(mapping[int(i)]))
            return int(''.join(n))
                
        nums.sort(key = mapped)
        return nums