# Quick Sort
# Quick Sort is another divide and conquer sorting algorithm that selects a pivot, partitions the array, and recursively sorts the partitions.

# Quick Sort Algorithm
# Select a pivot (typically the last element).
# Partition the array such that elements smaller than the pivot go to the left and greater ones go to the right.
# Recursively apply Quick Sort on the partitions.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5, 3, 8, 6, 2, 7]))  # Output: [2, 3, 5, 6, 7, 8]