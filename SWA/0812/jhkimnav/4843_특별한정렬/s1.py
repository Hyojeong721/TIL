import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N : 정수의 갯수
    # arr : 특별한 정렬을 할 정수 list
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, N):
        # 정렬할 idx
        sorting_idx = i
        # 최대값 찾기
        if i % 2 == 0:
            for j in range(i+1, N):
                if arr[j] > arr[sorting_idx]:
                    sorting_idx = j
        # 최솟값 찾기
        else:
            for j in range(i+1, N):
                if arr[j] < arr[sorting_idx]:
                    sorting_idx = j
        arr[i], arr[sorting_idx] = arr[sorting_idx], arr[i]

    print('#{} '.format(test_case), end='')
    for i in range(10):
        print(arr[i], end=' ')
    print()
