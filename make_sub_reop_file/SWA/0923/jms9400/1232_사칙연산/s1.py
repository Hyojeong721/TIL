import sys
sys.stdin = open('input.txt')

T = 10


def traversal(temp):
    i, n, a, b = temp
    for j in lst:
        if j[0] == a:
            if len(j) == 4:
                a = traversal(j)
            else:
                a = int(j[1])
        if j[0] == b:
            if len(j) == 4:
                b = traversal(j)
            else:
                b = int(j[1])
    if n == '+':
        return a + b
    elif n == '-':
        return a - b
    elif n == '*':
        return a * b
    elif n == '/':
        return a / b


for tc in range(1, T + 1):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    answer = int(traversal(lst[0]))

    print('#{} {}'.format(tc, answer))

# 1953.[모의 SW 역량테스트] 탈주범 검거
# 1952.[모의 SW 역량테스트] 수영장
# 1949.[모의 SW 역량테스트] 등산로 조성