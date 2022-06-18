import sys
sys.stdin = open('input.txt')


# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def search_7_digits_numbers(r, c, count, number):
    """
    주어진 2차원 배열에서 7자리 숫자를 모두 탐색한다. (완전 탐색)
    Args:
        r, c: 현재 탐색 위치
        count: 현재까지 탐색한 숫자의 길이 (int)
        number: 현재까지 탐색한 숫자 (str)
    """
    # 7자리 숫자를 모두 탐색했다면 => number_set에 숫자를 추가하고 탐색 종료
    if count == 7:
        global number_set
        number_set.add(number)
        return

    # 상하좌우에 숫자가 있는 경우 해당 숫자로 이동한 뒤, 탐색을 이어간다.
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            search_7_digits_numbers(nr, nc, count + 1, number + board[nr][nc])


T = int(input())

for x in range(1, T + 1):
    board = []

    for _ in range(4):
        board.append([x for x in input().split()])

    number_set = set()

    for r in range(4):
        for c in range(4):
            search_7_digits_numbers(r, c, 1, board[r][c])

    print("#{} {}".format(x, len(number_set)))
