import sys
sys.stdin = open('input.txt')

def solution(n):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        cnt = 0
        while n > money[i]:
            n -= money[i]
            cnt += 1
        used[i] = cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    used = [0] * 8
    solution(N)
    print('#{}'.format(tc))
    print(' '.join(map(str, used)))