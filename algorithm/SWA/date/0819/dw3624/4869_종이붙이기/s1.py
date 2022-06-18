import sys
sys.stdin = open('input.txt')

T = int(input())

# idea
# 경우의 수 구하는 함수
# 왼쪽을 채워가면서 함수 반복실행 --> 점화식


# 길이 n인 종이에 작은 종이, 큰 종이를 나열할 수 있는 경우의 수
def paper(n):
    # print('n:', n)
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n - 1) + paper(n - 2) * 2


for t in range(1, T+1):
    n = int(input())
    n = n // 10

    result = paper(n)
    print('#{} {}'.format(t, result))