import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    # N : 수열의 갯수
    # M : 작업 수
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    for _ in range(M):
        front = arr.pop(0)
        arr.append(front)

    print('#{} {}'.format(TC, arr.pop(0)))