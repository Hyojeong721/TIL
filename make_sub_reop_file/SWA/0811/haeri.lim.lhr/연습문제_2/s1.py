import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    # count = 0
    result = 0

    for i in range(1<<n):
        temp = []
        total = 0
        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])
        for k in temp:
            total += k
        if total == 0 and len(temp) > 0:
            result = 1
            break
            # count += 1

    print(result)