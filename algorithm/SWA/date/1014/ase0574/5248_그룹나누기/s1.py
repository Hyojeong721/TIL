# 3 / 10
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = []
    ans = 0

    for i in range(len(arr)//2):
        if (arr[i*2] not in result) & (arr[i*2+1] not in result):
            result.append(arr[i*2])
            result.append(arr[i*2+1])
            ans += 1
        else:
            result.append(arr[i*2])
            result.append(arr[i*2+1])
    for j in range(1, N+1):
        if j not in result:
            ans += 1


    print("#{} {}".format(tc, ans))

