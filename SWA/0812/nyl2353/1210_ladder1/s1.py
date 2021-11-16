import sys
sys.stdin = open('input.txt')

def choose_ladder(ladder, N=100):
    """
    사다리 게임의 도착지부터 거슬러 올라가 출발지를 찾는 함수
    ladder : 100 * 100 사다리

    """
    # 올라가기 시작할 좌표
    row = N - 1
    for i in range(N):
        if ladder[N - 1][i] == 2:
            col = i

    while row > 0:
        # 왼쪽 길 있으면, 쭉 가다가 막혔을 때 위로 한 칸
        if col != 0 and ladder[row][col - 1]:
            while col != 0 and ladder[row][col - 1]:
                col -= 1
            row -= 1
        # 오른쪽 길 있으면, 쭉 가다가 막혔을 때 위로 한 칸
        elif col != N - 1 and ladder[row][col + 1]:
            while col != N - 1 and ladder[row][col + 1]:
                col += 1
            row -= 1
        # 둘 다 길 없으면 위로 한 칸
        else:
            row -= 1

    return col

for tc in range(1, 11):
    N = int(input())
    test_case = []
    for i in range(100):
        test_case.append(list(map(int, input().split())))

    ladder = choose_ladder(test_case)
    print('#{0} {1}'.format(tc, ladder))

# 테스트용
# ladder = [
#     [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
#     [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 1, 0, 0, 2],
# ]
# result = choose_ladder(ladder, 10)
# print(result)