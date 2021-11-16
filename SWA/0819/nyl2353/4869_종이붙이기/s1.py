import sys
sys.stdin = open('input.txt')


# 종이 길이의 전 범위에 대해 미리 값을 구해놓음
# 종이의 가로 길이 M <= 300
memo = [0] * 31
memo[1] = 1
memo[2] = 3
for i in range(3, 31):
    memo[i] = memo[i-1] + 2 * memo[i-2]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = memo[N // 10]
    print('#{0} {1}'.format(tc, result))