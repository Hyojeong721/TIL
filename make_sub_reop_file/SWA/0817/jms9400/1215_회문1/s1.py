import sys
sys.stdin = open('input.txt')

T = 10

def check_palindrome(lst):
    result = 0
    for i in range(N//2):
        if lst[i] == lst[-(i+1)]:
            result += 1
    if result == (N//2):
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    N = int(input()) # 회문길이
    arr = [list(input()) for _ in range(8)]
    result = 0

    for i in range(8):
        for j in range(8-N+1):
            # 가로 회문
            if check_palindrome(arr[i][j:j+N]) == 1:
                result += 1
            # 세로 회문
            lst = []
            for k in range(N):
                lst.append(arr[j+k][i])
            if check_palindrome(lst) == 1:
                result += 1
    print('#{} {}'.format(tc, result))



