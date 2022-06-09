import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
cnt = 0

while cnt < N:
    temp = arr[cnt:]
    min_num = min(temp)
    for i in range(cnt, N):
        if arr[i] == min_num:
            min_num_idx = i
            break

    arr[cnt], arr[min_num_idx] = arr[min_num_idx], arr[cnt]
    cnt += 1
    if cnt != N-1:
        print(*arr)