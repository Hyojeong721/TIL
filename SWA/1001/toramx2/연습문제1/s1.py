def selectionsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def selection_recursive(arr, i, n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    if i + 1 < n:
        selection_recursive(arr, i+1, n)

    return arr


arr = [3, 5, 9, 7, 8, 6, 4, 1, 2]
print(selectionsort(arr))
print(selection_recursive(arr, 0, len(arr)))
