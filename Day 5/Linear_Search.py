def linear_search(arr, target):
    """
    Search for target in arr using linear search.
    Returns the index of target if found; otherwise, returns -1.
    """
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

# Test the linear_search function
numbers = [5, 3, 7, 1, 9, 2]
target = 7
result = linear_search(numbers, target)

if result != -1:
    print(f"Linear Search: Found {target} at index {result}.")
else:
    print(f"Linear Search: {target} not found in the list.")