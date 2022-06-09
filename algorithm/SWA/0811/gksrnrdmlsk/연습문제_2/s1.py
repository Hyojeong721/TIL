import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    result = 0
    lst = list(map(int, input().split()))
    n = len(lst)
    for i in range(1, 1 << n):
        total = 0
        for j in range(n):
            if i & (1 << j):
                total += lst[j]

        if total == 0:
            result = 1
            break

    print(result)