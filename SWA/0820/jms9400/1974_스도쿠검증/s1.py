import sys
sys.stdin = open('input.txt')

T = int(input())

def sudoku_chekcer(sudoku):
    checker1 = [0] * 9  # 가로
    checker2 = [0] * 9  # 세로
    checker3 = [0] * 9  # 격자상자
    # 여기에 만들필요 없이 for 문 안에서 만들면 계속 reset 해줄 필요없이 버리고 새로 만들면됨!!!

    # 가로 세로 검사
    for i in range(9):
        for j in range(9):
            checker1[sudoku[i][j]-1] = 1
            checker2[sudoku[j][i]-1] = 1

            # 격자검사
            # if i % 3 == 0 and j % 3 == 0:
            #     square = [0] * 10
            #     for r in range(i, i+3):
            #         for c in range(j, j+3):
            #             num = sudoku[r][c]
            #             if square[num]: return 0
            #             square[num] = 1

        for n in range(9):
            if checker1[n] == 0 or checker2[n] == 0:
                return 0
            else:
                checker1[n] = 0
                checker2[n] = 0


    # 격자 검사
    cnt = 0
    for j in range(0, 9, 3):
        for i in range(9):
            for k in range(j, j+3):
                checker3[sudoku[i][k]-1] = 1
                cnt += 1

            if cnt == 9:
                for n in range(9):
                    if checker3[n] == 0:
                        return 0
                    else:
                        checker3[n] = 0
                cnt = 0
    return 1




for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, sudoku_chekcer(sudoku)))

