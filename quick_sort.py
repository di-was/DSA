def quick_sort(array):

    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    
    left_partition, right_partition = [], []

    for x in range(len(array) - 1):
        if array[x] < pivot:
            left_partition.append(array[x])
        else:
            right_partition.append(array[x])


    left_partition = quick_sort(left_partition)
    right_partition = quick_sort(right_partition)

    return left_partition + [pivot] + right_partition 

print(quick_sort([1, 2, 3, 8, 4, 5, 6, 7, 9]))