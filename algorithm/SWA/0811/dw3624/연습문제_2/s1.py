import sys
sys.stdin= open('input.txt')

T = int(input())

for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    n = len(arr)

    result = 0
    for i in range(1, 1<<n):
        val = 0
        for j in range(n):
            if i & (1<<j):
                val += arr[j]
        if val == 0:
            result = 1
            break

    print('#{} {}'.format(t, result))