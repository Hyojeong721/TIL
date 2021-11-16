import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers), 0, -1):
        for j in range(i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print('#{}'.format(t), end = ' ')
    for k in range(1, 5 + 1):
        print(numbers[-k], end = ' ')
        print(numbers[k-1], end = ' ')
    print()