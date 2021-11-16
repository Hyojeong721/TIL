import sys
sys.stdin = open ('input.txt')
# 08.24
T = int(input())

for tc in range(1,T+1):
    # n: 구역 / m: 파리채사이즈
    n, m= list(map(int, input().split()))
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    max_res = 0

    for row in range(n-m+1):
        for col in range(n-m+1):
            result = 0
            for i in range(m):
                for j in range(m):
                    result += arr[row + i][col + j]

            if result > max_res:
                max_res = result

    print("#{} {}".format(tc, max_res))






