import sys
sys.stdin = open('input.txt')

T = int(input())

def check_palindrome(lst):
    result = 0
    for i in range(M//2):
        if lst[i] == lst[-(i+1)]:
            result += 1
    if result == (M//2):
        return 1
    else:
        return 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = []


    if N == M:
        for i in range(N):
            # 가로 회문
            if check_palindrome(arr[i]) == 1:
                result = arr[i]
                break
            # 세로 회문
            else:
                my_lst = []
                for j in range(N):
                    my_lst.append(arr[j][i])
                if check_palindrome(my_lst) == 1:
                    result = my_lst
                    break
    else:
        for i in range(N):
            for j in range(N-M+1):
                # 가로 회문
                if check_palindrome(arr[i][j:j+M]):
                    result = arr[i][j:j+M]
                    break
                # 세로 회문
                else:
                    my_lst = []
                    for k in range(j, j+M):
                        my_lst.append(arr[k][i])
                    if check_palindrome(my_lst) == 1:
                        result = my_lst
                        break
    print('#{} {}'.format(tc, ''.join(result)))

# N, M 길이 굳이 체크하지않을 수 있도록 통합해보기