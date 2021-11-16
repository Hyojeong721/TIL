import sys
sys.stdin = open('input.txt')
# N x N 행렬이 주어질 때,
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
T = int(input())
for tc in range(1, T+1):
    # N은 3 이상 7 이하이다.
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    # 90도= 각 행의 첫번째 숫자들(역순)
    ans_90 = []
    result_90 = []

    for g in range(N):
        for i in range(N-1, -1, -1):
            result_90.append(arr[i][g])
        if len(result_90) == N:
            a = ''.join(result_90)
            ans_90.append(a)
            result_90=[]

    # 180도= 마지막행의 역순
    ans_180 = []
    result_180 = []
    for r in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            result_180.append(arr[r][j])
        if len(result_180) == N:
            a = ''.join(result_180)
            ans_180.append(a)
            result_180 = []

    # 270도= 마지막 열
    ans_270 = []
    result_270 = []
    for c in range(N-1, -1, -1):
        for k in range(N):
            result_270.append(arr[k][c])
        if len(result_270) == N:
            a = ''.join(result_270)
            ans_270.append(a)
            result_270 = []

    print("#{}".format(tc))
    for i in range(N):
        print(ans_90[i], ans_180[i], ans_270[i])

