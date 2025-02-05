def bubble_sort(arr):
    """
    Sort the array using the bubble sort algorithm.
    Returns a new sorted list.
    """
    n = len(arr)
    sorted_arr = arr.copy()  # Create a copy to avoid modifying the original list
    for i in range(n):
        # Track whether any swap happened; if not, the list is sorted.
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, break early
        if not swapped:
            break
    return sorted_arr

# Test the bubble_sort function
unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", unsorted_numbers)
sorted_numbers = bubble_sort(unsorted_numbers)
print("Sorted List (Bubble Sort):", sorted_numbers)