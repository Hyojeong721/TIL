import sys
sys.stdin = open('input.txt')


def quicksort(l, r):
    global lst

    if l < r:
        s = lomuto_partition(l, r)
        quicksort(l, s-1)
        quicksort(s+1, r)

def hoare_partition(l, r):
    global lst

    p = lst[l]
    i = l
    j = r

    while i <= j:
        while i <= j and lst[i] <= p:
            i += 1
        while i <= j and lst[j] >= p:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    return j

def lomuto_partition(l, r):
    global lst

    p = lst[r]
    i = l-1

    for j in range(l, r):
        if lst[j] <= p:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
        j += 1

    lst[r], lst[i+1] = lst[i+1], lst[r]
    return i+1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quicksort(0, N-1)
    print('#{} {}'.format(tc, lst[N//2]))