import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # set()를 사용하여 중복문자 제거
    N = list(set(input()))
    M = list(input())
    str_count = [0] * len(N)

    # M에 포함된 N의 각 문자의 갯수 카운트
    for i in M:
        for j in range(len(N)):
            if i == N[j]:
                str_count[j] += 1

    print('#{0} {1}'.format(tc, max(str_count)))