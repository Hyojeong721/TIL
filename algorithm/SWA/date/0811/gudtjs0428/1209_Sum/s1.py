import sys
sys.stdin = open('input.txt')

def get_biggest_line(matrix):
    biggest_line = 0
    # for row in matrix:
    #     if sum(row) > biggest_line:
    #         biggest_line = sum(row)

    rows = []
    columns = []
    diagonal_from_left = 0
    diagonal_from_right = 0
    for i in range(len(matrix)):
        rows.append(sum(matrix[i]))

        total = 0
        for j in range(len(matrix)):
            total += matrix[j][i]
        columns.append(total)

        diagonal_from_left += matrix[i][i]
        diagonal_from_right += matrix[i][99-i]

    sum_of_lines = []
    sum_of_lines.extend(rows)
    sum_of_lines.extend(columns)
    sum_of_lines.extend([diagonal_from_right, diagonal_from_right])
    return max(sum_of_lines)


T = 10
for tc in range(1, T + 1):
    input()
    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, get_biggest_line(matrix)))