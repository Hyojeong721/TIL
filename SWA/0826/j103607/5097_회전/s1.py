import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # N개의 숫자, M번 작업 반복
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for i in range(M):
        a = numbers.pop(0)
        numbers.append(a)

    print('#{} {}'.format(tc, numbers[0]))