def binary_search(array, target):
    if not array:
        return -1
    
    mid_point = len(array) // 2
    if array[mid_point] == target:
        return mid_point
    elif array[mid_point] < target:
        result = binary_search(array[mid_point:], target)
        if result == -1:
            return -1
        else:
            return  mid_point + result
    elif array[mid_point] > target:
        return binary_search(array[0:mid_point], target) 


print(binary_search([1, 2, 3, 4, 5, 6], 3))
    