import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(0, T):
    N = int(input())
    a = list(map(int, input().split()))
    max = 0
    min = 1000001
    for j in a:
        if j > max:
            max = j
        if j < min:
            min = j
    print(f'{i} {max - min}')
