import sys
sys.stdin = open('input.txt')


def cargo_calender(board):
    sorted_list = sorted(board, key=lambda cargo: cargo[1])

    cargo_schedule = [sorted_list[0]]

    for cargo in sorted_list:
        if cargo[0] >= cargo_schedule[-1][1]:
            cargo_schedule.append(cargo)
    return cargo_schedule

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [tuple(map(int, input().split())) for _ in range(N)]

    print("#{} {}".format(tc, len(cargo_calender(board))))