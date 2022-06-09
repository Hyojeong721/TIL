import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []

    for i in m:
        tmp = 0
        while N >= i:
            N -= i
            tmp += 1
        answer.append(tmp)

    print('#{}'.format(tc))
    print(' '.join(map(str, answer)))