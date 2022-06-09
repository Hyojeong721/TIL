import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
cnt = 1

while cnt < N:
    num = arr[cnt]
    for i in range(cnt):
        if arr[i] > num:
            arr.pop(cnt)
            arr.insert(i, num)
            break

    cnt += 1
    print(*arr)