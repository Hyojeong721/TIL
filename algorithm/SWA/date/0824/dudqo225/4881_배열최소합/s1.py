import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]


    total = 0
    stack = []
    for i in range(N):
        min_value = arr[i][0]
        for j in range(N):
            if arr[i][j] <= min_value:
                min_idx = j
                if min_idx not in stack:
                    min_value = arr[i][j]

        stack.append(min_idx)
        total += min_value


    print(total)