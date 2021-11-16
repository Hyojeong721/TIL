import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    n = int(input())
    a = [input() for _ in range(T-2)]
    result = 0
    for i in range(8):

        # 가로 탐색
        for j in range(8-n+1):
            if a[i][j:j+n] == a[i][j:j+n][::-1]:
                result += 1

        # 세로 탐색
        for j in range(8-n+1):
            # 빈 tmp에 문자열 넣어서 비교
            tmp = []
            for k in range(n):
                tmp.append(a[j+k][i])
            if tmp == tmp[::-1]:
                result += 1

    print("#{} {}".format(tc, result))