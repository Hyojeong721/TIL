import sys
sys.stdin = open('input.txt')


def get_max_value(board, exchange, fix_idx):
    """
    Args:
        board: 현재 수 배열 (ex. ['5', '9', '7', '3'])
        exchange: 남은 교환 횟수
        fix_idx: 자리가 확정된 마지막 숫자의 인덱스
    """
    global N, max_value

    # 교환 횟수를 모두 사용한 경우
    if not exchange:
        max_value = max(max_value, int(''.join(board)))
        return

    # 자리가 fix되지 않은 숫자들에 대하여
    # 뒤에서부터 그 숫자까지의 가장 큰 숫자를 배열로 저장한다.
    highest_arr = [0] * N
    highest_arr[-1] = board[-1]

    for i in range(N - 2, fix_idx, -1):
        highest_arr[i] = max(highest_arr[i + 1], board[i])

    # 맨 앞자리가 현재까지 가장 높은 숫자와 같다면, 그 자리를 fix시킨다.
    while fix_idx + 1 < N and board[fix_idx + 1] == highest_arr[fix_idx + 1]:
        fix_idx += 1

    # 모든 숫자의 위치가 확정된 경우 (더 이상 값을 증가시킬 수 없는 경우)
    if fix_idx >= N - 2:
        """
        A. 같은 숫자가 존재한다면 => 해당 숫자들끼리 바꾸면 값을 유지할 수 있다.
        B. 남은 교환 횟수가 짝수라면 => 숫자를 2번씩 교환하여 값을 유지할 수 있다.
        A와 B에 모두 해당하지 않는 경우만, 마지막 두 수의 값을 바꾸어준다. 
        (한번 교환한 이후, 남은 교환 횟수는 짝수이므로 B가 된다.)
        """
        if exchange % 2 == 1 and list(set(board)) == board:
            board[-1], board[-2] = board[-2], board[-1]
            max_value = max(max_value, int(''.join(board)))
            board[-1], board[-2] = board[-2], board[-1]
        else:
            max_value = max(max_value, int(''.join(board)))
        return

    # 확정되지 않는 맨 앞 숫자와 그 뒤의 모든 숫자들을 교환하는 경우를 탐색한다.
    for j in range(fix_idx + 2, N):
        board[j], board[fix_idx + 1] = board[fix_idx + 1], board[j]
        get_max_value(board, exchange - 1, fix_idx + 1)
        board[j], board[fix_idx + 1] = board[fix_idx + 1], board[j]


T = int(input())

for C in range(1, T + 1):
    board, exchange = map(int, input().split())
    board = list(str(board))
    N = len(board)
    max_value = 0

    get_max_value(board, exchange, -1)
    print("#{} {}".format(C, max_value))