# 0829
import sys
sys.stdin = open('input.txt')

def ans(arr):
    global N, K
    result = 0
    ans = []
    cnt = 0
    # 행검사
    for i in range(N):
        result = 0
        for j in range(N):
            if arr[i][j] == 1:
                result += 1
                if j == N-1:
                    ans.append(result)
            else:
                if result != 0:
                    ans.append(result)
                result = 0

    # 열검사
    for i in range(N):
        result = 0
        for j in range(N):
            if arr[j][i] == 1:
                result += 1
                if j == N-1:
                    ans.append(result)
            else:
                if result != 0:
                    ans.append(result)
                result = 0

    # 문자길이와 같은 공간 갯수 찾기
    for w in ans:
        if w == K:
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    # N x N 행렬 / K 넣을 글자 길이
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    print("#{} {}".format(tc, ans(arr)))
