import sys
sys.stdin = open('input.txt')

def count_palindrome(N, matrix):
    count = 0
    for i in range(8):
        for j in range(8 - N + 1):
            check1 = 1      # 가로에 회문 존재시
            check2 = 1      # 세로에 회문 존재시
            k = 0
            while k < N//2:
                if matrix[i][j + k] == matrix[i][j + N - 1 - k]:
                    k += 1
                else:
                    check1 = 0
                    break
            k = 0
            while k < N//2:
                if matrix[j + k][i] == matrix[j + N - 1 - k][i]:
                    k += 1
                else:
                    check2 = 0
                    break
            if check1 == 1:
                count += 1
            if check2 == 1:
                count += 1
    return count

T = 10
for tc in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(8)]
    print('#{} {}'.format(tc, count_palindrome(N, matrix)))