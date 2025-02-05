# Important: Binary search works only on sorted lists.
def binary_search(sorted_arr, target):
    """
    Search for target in sorted_arr using binary search.
    Returns the index of target if found; otherwise, returns -1.
    """
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test the binary_search function
sorted_numbers = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(sorted_numbers, target)

if result != -1:
    print(f"Binary Search: Found {target} at index {result}.")
else:
    print(f"Binary Search: {target} not found in the list.")