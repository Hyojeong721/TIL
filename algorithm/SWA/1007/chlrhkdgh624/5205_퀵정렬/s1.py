import sys
sys.stdin = open('input.txt')


def quick_sort(arr, left, right):
    if left < right:
        pivot = hoare(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)


def hoare(arr, left, right):
    pivot = arr[left]
    i = left
    j = right
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N-1)
    result = numbers[N//2]
    print(f'#{tc} {result}')