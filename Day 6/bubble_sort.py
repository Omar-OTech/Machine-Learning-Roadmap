# Sorting Algorithms
# Sorting is the process of arranging elements in ascending or descending order. There are many sorting techniques, each with different efficiency levels.

# Bubble Sort (Simple but Inefficient)
# Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:    # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


print(bubble_sort([5, 1, 4, 2, 8]))  # Output: [1, 2, 4, 5, 8]