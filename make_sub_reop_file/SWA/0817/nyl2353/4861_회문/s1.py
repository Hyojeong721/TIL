import sys
sys.stdin = open('input.txt')

def get_palindrome(N, M, mat):
    for r in range(N):
        for c in range(N - M + 1):
            start = 0
            end = M - 1
            cnt = 0
            while start < end:
                if mat[r][c + start] == mat[r][c + end]:
                    start += 1
                    end -= 1
                    cnt += 1
                else:
                    break
            if cnt == M // 2:
                result = ""
                for i in range(M):
                    result += mat[r][c + i]
                return result

    for c in range(N):
        for r in range(N - M + 1):
            start = 0
            end = M - 1
            cnt = 0
            while start < end:
                if mat[r + start][c] == mat[r + end][c]:
                    start += 1
                    end -= 1
                    cnt += 1
                else:
                    break
            if cnt == M // 2:
                result = ""
                for i in range(M):
                    result += mat[r + i][c]
                return result


T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    mat = []
    for _ in range(N):
        row = list(input())
        mat.append(row)
    result = get_palindrome(N, M, mat)
    print('#{0} {1}'.format(tc, result))