import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = min(trees), max(trees)
res = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for t in trees:
        if t > mid:
            temp += (t-mid)

    if temp >= M:
        start = mid+1
    else:
        end = mid-1

print(end)