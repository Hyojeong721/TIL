import sys
sys.stdin = open('input.txt')

def how_many_words(N, K, matrix):
    count = 0
    for i in range(N):
        for j in range(N-K+1):
            if j == 0:
                if matrix[i][:K] == [1] * K and matrix[i][K] == 0:
                    count += 1
                check = 1
                for k in range(K):
                    if matrix[k][i] != 1:
                        check = 0
                        break
                if check == 1 and matrix[K][i] == 0:
                    count += 1
            elif j == N - K:
                if matrix[i][j-1] == 0 and matrix[i][j:j+K] == [1] * K:
                    count += 1
                check = 1
                for k in range(K):
                    if matrix[j+k][i] != 1:
                        check = 0
                        break
                if check == 1 and matrix[j-1][i] == 0:
                    count += 1
            else:
                if matrix[i][j-1] == 0 and matrix[i][j:j+K] == [1] * K and matrix[i][j+K] == 0:
                    count += 1
                check = 1
                for k in range(K):
                    if matrix[j+k][i] != 1:
                        check = 0
                        break
                if check == 1 and matrix[j-1][i] == 0 and matrix[j+K][i] == 0:
                    count += 1

    return count


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, how_many_words(N, K, matrix)))