# Merge Sort (Efficient)
# Merge Sort is a divide and conquer algorithm that splits the list into halves, sorts them, and merges them back.

def merge_sort(arr):
    if len(arr) <= 1: # Base case
        return arr
    mid = len(arr) // 2
    # print('mid:', mid)
    left_half = merge_sort(arr[:mid])
    # print('left_half:', left_half)
    right_half = merge_sort(arr[mid:])
    # print('right_half:', right_half)
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

print(merge_sort([5, 3, 8, 6, 2, 7]))  # Output: [2, 3, 5, 6, 7, 8]