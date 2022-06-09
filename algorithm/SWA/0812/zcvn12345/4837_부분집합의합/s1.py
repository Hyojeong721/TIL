import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    arr = list(range(1, 13))
    N, K = map(int, input().split())
    count = 0
    for i in range(1<<12):
        arr_son = []
        for j in range(13):
            if i & (1<<j):
                arr_son.append(arr[j])

        if len(arr_son) == N and sum(arr_son) == K:
            count += 1

    print('#{0} {1}'.format(test_case, count))

