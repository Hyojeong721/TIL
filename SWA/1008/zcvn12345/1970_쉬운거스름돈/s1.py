import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    while N >= 10:
        for i in range(8):
            if N >= money[i]:
                N -= money[i]
                count[i] += 1
                break
    print(f'#{tc}')
    for j in count:
        print(j, end=' ')
    print()