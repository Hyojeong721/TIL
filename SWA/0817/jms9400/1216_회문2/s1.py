import sys
sys.stdin = open('input.txt')

T = 10

def check_palindrome(lst):
    N = len(lst)
    for i in range(N//2):
        if lst[i] != lst[-(i+1)]:
            return 0
    return 1

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    result = 0
    m = 100 # 가로 회문 길이

    # 가로 회문 확인 - 길이 100부터 차례대로 내려가도록
    while m >= 0:
        breaker = 0
        for i in range(100):
            for j in range(100):
                if j+m in range(101) and arr[i][j] == arr[i][j+m-1]:
                    if check_palindrome(arr[i][j:j+m]) == 1:
                        result = m
                        breaker = 1
                        break
            if breaker == 1:
                break
        if breaker == 1:
            break
        m -= 1
    print(result)

    n = result + 1 # 세로 회문 길이
    lst = []
    # 세로 회문 확인 - 가로 최대 회문 길이부터 차례대로 올라가도록
    while n <= 100:
        for i in range(100):
            for j in range(100-n+1):
                if arr[j][i] == arr[j+n-1][i]:
                    for k in range(n):
                        lst.append(arr[j+k][i])
                    if check_palindrome(lst) == 1:
                        result = n
                    lst = []
        n += 1

    print('#{} {}'.format(tc, result))