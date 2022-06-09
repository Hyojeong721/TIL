import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)

    i = 0
    cnt = 0
    while i < len(arr):
        t = arr[i]
        temp = []
        for k in range(i+1, i+t+1):
            temp.append((arr[k]+k, arr[k], k))
        temp.sort()
        a, t, i = temp.pop()
        cnt += 1
        if i + t >= len(arr):
            break

    print('#{} {}'.format(tc, cnt))