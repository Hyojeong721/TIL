# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고,
# A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.
import sys
sys.stdin = open('input.txt')

def quick_sort(l, r):
    global arr

    if l >= r:
        return

    p = l
    i = l + 1
    j = r

    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1

        while i <= j and arr[j] >= p:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]

    quick_sort(l, j - 1)
    quick_sort(j + 1, r)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N-1)
    print("#{} {}".format(tc, arr[N//2]))

