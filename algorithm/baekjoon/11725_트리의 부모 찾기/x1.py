import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [0 for _ in range(N+1)]
arr[1] = 1


for i in range(N-1):
    a, b = map(int, input().split())
    if arr[a] == 0 and arr[b] != 0:
        arr[a] = b
    if arr[a] != 0 and arr[b] == 0:
        arr[b] = a

for k in range(2, N+1):
    print(arr[k])