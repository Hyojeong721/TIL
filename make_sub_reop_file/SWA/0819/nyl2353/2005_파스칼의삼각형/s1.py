import sys
sys.stdin = open('input.txt')


# 1. memoization
# 삼각형 크기: 1 <= N <= 10
tri = [[1] for _ in range(10)]
tri[1].append(1)
for r in range(2, 10):
    for c in range(1, r + 1):
        if c == r:
            tri[r].append(1)
        else:
            value = tri[r - 1][c - 1] + tri[r - 1][c]
            tri[r].append(value)


# 2. 삼각형 출력하는 함수
def get_triangle(N):
    global tri

    for i in range(N):
        for num in tri[i]:
            print(num, end=' ')
        print()


# 3. test case 별로 출력
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    get_triangle(N)