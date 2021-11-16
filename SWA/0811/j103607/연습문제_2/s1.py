import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):

    numbers = list(map(int, input().split()))
    N = len(numbers) #10

    count = 0
    for i in range(1<<N):
        sumV = 0
        for j in range(N):
            if i & (1<<j):
                sumV += numbers[j]

        if sumV == 0:
            count += 1

    print('#{} {}'.format(tc, count))
