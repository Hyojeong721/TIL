import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
names = []
arr = [deque() for _ in range(21)]
# 이름 길이를 저장함 / 들어오는 순서 = 등수
for n in range(N):
    names.append(len(sys.stdin.readline()))

cnt = 0

# i:등수 / v:이름길이
for i, v in enumerate(names):
    # 이름길이 리스트에
    while arr[v] and i-arr[v][0] > K:
        arr[v].popleft()

    if arr[v]:
        cnt += len(arr[v])

    arr[v].append(i)

print(cnt)