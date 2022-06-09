import sys
sys.stdin = open("input.txt")


def count_word(board, size, word_len):
    """
    주어진 퍼즐 모양에 특정 길이를 갖는 단어가 들어갈 수 있는 자리를 구한다.
    단어는 단어 길이와 딱 맞는 경우에만 들어갈 수 있다.
    (ex. 5칸 연속 빈 칸인 경우 3자리 단어를 넣을 수 없다.)

    board: 퍼즐의 모양 (2차원 배열)
    size: board의 가로, 세로 길이
    word_len: 단어의 길이

    count: 퍼즐에 들어갈 수 있는 단어의 개수
    length: 단어가 들어갈 빈칸의 길이
    """
    count = 0

    # 1. 가로 탐색
    for r in range(size):
        length = 0

        for c in range(size):
            # board[r][c]가 빈칸이라면
            if board[r][c]:
                length += 1
            # board[r][c]가 빈칸이 아니라면
            else:
                # 이전 칸까지의 빈칸 길이가 찾는 단어의 길이인지 확인한다.
                if length == word_len:
                    count += 1
                length = 0

        # 마지막 칸까지의 빈칸 길이가 찾는 단어의 길이인지 확인한다.
        if length == word_len:
            count += 1

    # 2. 세로 탐색
    for c in range(size):
        length = 0

        for r in range(size):
            if board[r][c]:
                length += 1
            else:
                if length == word_len:
                    count += 1
                length = 0

        if length == word_len:
            count += 1

    return count


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    word_count = count_word(board, N, K)
    print("#{} {}".format(tc, word_count))
