import sys
sys.stdin = open('input.txt')

T = 10

def in_order(n):
    global answer
    if n <= N:
        in_order(n*2)
        for i in lst:
            if int(i[0]) == n:
                answer += i[1]
        in_order(n*2+1)

for tc in range(1, T + 1):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    answer = ''
    in_order(1)
    print('#{} {}'.format(tc, answer))