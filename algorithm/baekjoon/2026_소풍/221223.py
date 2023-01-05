import sys
input = sys.stdin.readline


K, N, F = map(int, input().split())
arr = [[0] * (N+1)]
for _ in range(F):
    s, t = map(int, input().split())
    arr[s].append(t)
    arr[t].append(s)

for n in range(N):
    print(arr[n])
