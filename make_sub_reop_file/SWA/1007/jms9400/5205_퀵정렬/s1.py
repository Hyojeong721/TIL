import sys
sys.stdin = open('input.txt')

T = int(input())

def quicksort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quicksort(lst, l, s-1)  # 피봇보다 작은
        quicksort(lst, s+1, r)   # 피봇보다 큰
    return lst

def partition(lst, l, r):  # hoare
    p = lst[l]
    i = l
    j = r
    while i <= j:
        while i <= j and lst[i] <= p:  # 피봇보다 큰 값 만날 때까지
            i += 1
        while i <= j and lst[j] >= p:  # 피봇보다 작은 값 만날 때까지
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    # 경계구역이 정해짐짐
    lst[l] lst[j] = lst[j], lst[l]
    return j

def loumuto_p(A, l, r):
    pivot = A[r]
    i = l-1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quicksort(arr, 0, N-1)

    print('#{} {}'.format(tc, arr[N//2]))
