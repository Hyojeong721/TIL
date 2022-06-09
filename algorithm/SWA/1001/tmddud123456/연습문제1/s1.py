def selectionSort(sort_list, length):
    for i in range(length-1):
        if sort_list[i] > sort_list[i+1]:
            sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
            print(sort_list)
            sort_list = selectionSort(sort_list, i+1)
    return sort_list


A = [9, 13, 1, 4, 6, 7, 8]
print(selectionSort(A, len(A)))