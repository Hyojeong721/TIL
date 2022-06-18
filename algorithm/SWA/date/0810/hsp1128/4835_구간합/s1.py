import sys
sys.stdin = open("input.txt")

T = int(input())
tc = 0

while tc < T:
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_num = 0
    min_num = 0
    for i in range(M):
        max_num += numbers[i]
        min_num += numbers[i]


    for i in range(N-M+1):
        total = 0
        for j in range(M):
            total += numbers[i+j]
        if total > max_num:
            max_num = total
        elif total < min_num:
            min_num = total
    result = max_num - min_num
    print(f'#{tc+1} {result}')
    tc += 1