import sys
sys.stdin = open('input.txt')

N = int(input())

temp = [i for i in range(1, N)]
ans = 0
for k in temp:
    arr = list(map(int, str(k)))
    res = k
    for i in range(len(arr)):
        res += arr[i]

    if res == N:
        ans = k
        break

print(ans)