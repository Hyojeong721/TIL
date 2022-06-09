def SelectionSort(k):
    if k == n-1:
        return
    else:
        minI = k
        for i in range(k+1, n):
            if lst[i] < lst[minI]:
                minI = i
        lst[k], lst[minI] = lst[minI], lst[k]
        SelectionSort(k+1)


lst = [3, 4, 1, 7, 8, 2]
n = len(lst)
SelectionSort(0)
print(lst)