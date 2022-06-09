def SelectionSort(A):
    n = len(A)

    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


def f(A, i, n):
    if i == n:
        return

    else:
        min_idx = i
        for k in range(i+1, n):
            if A[min_idx] > A[k]:
                min_idx = k
        A[i], A[min_idx] = A[min_idx], A[i]
        f(A, i+1, n)




A = [4, 3, 7, 1, 2, 9, 8]
# SelectionSort(A)
f(A, 0, len(A))
print(A)
