class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        introsort(nums)
        return nums
        
def introsort(arr):
    # Set maximum recursion depth to log2(len(arr)) * 2
    max_depth = math.ceil(math.log2(len(arr))) * 2
    introsort_helper(arr, 0, len(arr) - 1, max_depth)

def introsort_helper(arr, start, end, max_depth):
    # Use insertion sort for small arrays
    if end - start <= 15:
        insertion_sort(arr, start, end)
        return

    # Use heapsort for large arrays
    if max_depth == 0:
        heapsort(arr, start, end)
        return

    # Choose a pivot and partition the array
    pivot_index = choose_pivot(arr, start, end)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    partition_index = i + 1

    # Recursively sort the partitions
    introsort_helper(arr, start, partition_index - 1, max_depth - 1)
    introsort_helper(arr, partition_index + 1, end, max_depth - 1)

def choose_pivot(arr, start, end):
    # Choose pivot as median of first, middle, and last element
    mid = (start + end) // 2
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]
    return mid

def insertion_sort(arr, start, end):
    for i in range(start+1, end+1):
        j = i
        while j > start and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def heapsort(arr, start, end):
    # Build a max heap
    heap_size = end - start + 1
    for i in range(start + heap_size // 2, start - 1, -1):
        heapify(arr, start, end, i)

    # Extract elements from the heap in sorted order
    for i in range(end, start, -1):
        arr[start], arr[i] = arr[i], arr[start]
        heap_size -= 1
        heapify(arr, start, start + heap_size - 1, start)

def heapify(arr, start, end, i):
    largest = i
    left = start + 2 * (i - start) + 1
    right = start + 2 * (i - start) + 2

    if left <= end and arr[left] > arr[largest]:
        largest = left

    if right <= end and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, start, end, largest)
