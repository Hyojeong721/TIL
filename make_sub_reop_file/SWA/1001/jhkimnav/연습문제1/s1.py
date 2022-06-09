def select_sort(arr, idx, n):
    if idx == n:
        print(arr)
        return
    else:
        min_idx = idx
        for i in range(idx+1, n):
            if arr[min_idx] > arr[i]:
                min_idx = i
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        select_sort(arr, idx+1, n)


A = [5, 4, 3, 2, 6, 1]
N = len(A)
select_sort(A, 0, N)