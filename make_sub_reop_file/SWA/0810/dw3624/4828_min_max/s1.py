import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = numbers[N-1] - numbers[0]
    print('#{} {}'.format(t, result))