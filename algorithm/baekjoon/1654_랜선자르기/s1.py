import sys
sys.stdin = open("input.txt")

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
start, end = 1, max(arr)
res = 0

while start <= end:
    temp = 0

    mid = (start + end) // 2

    for k in arr:
        temp += (k // mid)


    if temp >= N:
        start = mid+1
    else:
        end = mid-1

print(end)