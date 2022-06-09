import sys
sys.stdin = open('input.txt')

def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return paper(n-2) * 2 + paper(n-1)

T = int(input())

for TC in range(1, T+1):
    answer = 0

    N = int(input())

    # N : 10의 배수
    answer = paper(N/10)

    print('#{} {}'.format(TC, answer))

