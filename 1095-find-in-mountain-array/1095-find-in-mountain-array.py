# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 1, n - 2
        while left < right:
            mid = (left + right) // 2
            leftEle = mountain_arr.get(mid - 1)
            midEle = mountain_arr.get(mid)
            rightEle = mountain_arr.get(mid + 1)
            if leftEle < midEle < rightEle:
                left = mid + 1
            elif leftEle > midEle > rightEle:
                right = mid - 1
            else:
                break
        peak = (left + right) // 2

        def binSearch(lo: int, hi: int, isLeftSlope: int = True) -> int:
            while lo <= hi:
                mid = (lo + hi) // 2
                midEle = mountain_arr.get(mid)
                if midEle < target:
                    if isLeftSlope:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                elif midEle > target:
                    if isLeftSlope:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    return mid
            return -1

        leftSearch = binSearch(0, peak)
        if leftSearch != -1:
            return leftSearch
        return binSearch(peak + 1, n - 1, False)