def binarySearch(nums: list, target: int) -> int:
    n = len(nums)
    low = 0
    high = n
    mid = n//2
    while -1 < mid < n:
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            return mid
        if mid == (low + high)//2:
            break
        else:
            mid = (low + high)//2
    return -1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                if binarySearch(i, target) > -1:
                    return True
                else:
                    return False
        return False