import sys
sys.stdin = open("input.txt")

T = int(input())
print(T)
for t in range(1,T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    for i in range(1, 1 << N):
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += arr[j]
        if total == 0:
            print('#%s 1' % t)
            break
    else:
        print('#%s 0' % t)