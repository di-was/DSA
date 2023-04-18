def binary_search(arr, target):
    if not arr:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        result = binary_search(arr[mid+1:], target)
        if result == -1:
            return -1
        else:
            return mid + 1 + result
    else:
        return binary_search(arr[:mid], target)