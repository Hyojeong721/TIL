import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    count = 0
    for i in range(1<<n):
        arr_son = []
        for j in range(n+1):
            if i & (1<<j):
                arr_son.append(arr[j])
        if sum(arr_son) == 0:
            count += 1

    if count > 1:
        print('#{0} 1'.format(test_case))
    else:
        print('#{0} 0'.format(test_case))




