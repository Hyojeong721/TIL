def SelectionSort(arr, i, N):
    if i == N:
        print(arr)
    else:
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        SelectionSort(arr, i+1, N)

SelectionSort([3, 9, 2, 5, 4, 10, 1, 8, 7, 6], 0, 10)


