import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):

    # N*N = 보드 크기   # M*M = 파리채 크기
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N-M+1): # 0, 1, 2, 3
        for j in range(N-M+1): # 0, 1, 2, 3

            # [i][j]를 기준으로 파리채 범위를 돌면서 범위 내의 파리 수를 flies에 더함
            flies = 0
            for a in range(M):
                for b in range(M):
                    flies += board[i+a][j+b]
                    result.append(flies)

    # 죽은 파리 수 리스트에서 가장 큰 값을 maxV로
    maxV = 0
    for flies in result:
        if maxV < flies:
            maxV = flies

    print('#{} {}'.format(tc, maxV))


'''
N=5 M=2
[0,0] + [0,1] + [1,0] + [1,1}
[0,1] + [0,2] + [1,1] + [1,2]
[0,2] + [0,3] + [1,2] + [1.3]
[0,3] + [0,4] + [1,3] + [1,4]

[1.0] + [1,1] + [2,0] + [2.1]
[1,1] + [1,2] + [2,1] + [2,2]

'''
