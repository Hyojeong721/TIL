import sys
sys.stdin = open('input.txt', 'r')
# 선택 정렬로 접근, runtime error 발생


def selection_sort(arr, cnt):
    n = len(arr)
    i = 0
    while cnt > 0 and i < n:
        max_i = i
        for j in range(n-1, i, -1):
            if arr[j] > arr[max_i]:
                max_i = j
        if max_i != i:
            arr[i], arr[max_i] = arr[max_i], arr[i]
            cnt -= 1
        i += 1
    else:
        if cnt == 0:
            return
        else:
            if cnt % 2 == 0:
                arr[n-2], arr[n-1] = arr[n-1], arr[n-2]


T = int(input())
for tc in range(1, T+1):
    numbers, count = input().split()
    numbers = list(map(int, numbers))
    count = int(count)
    selection_sort(numbers, count)
    numbers = list(map(str, numbers))
    result = ''.join(numbers)
    print(f'#{tc} {result}')











