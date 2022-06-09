# 시간도 초과고 답도 부정확,,,
import sys
sys.stdin = open('input.txt')

def min_total(lst):
    if len(lst) == 2:
        return min([lst[0][0] + lst[1][1], lst[0][1] + lst[1][0]])

    length = len(lst)
    temp = [(0, 0)]

    for r in range(length):
        for c in range(length):
            if lst[r][c] < lst[temp[0][0]][temp[0][1]]:
                temp = [(r, c)]
            elif lst[r][c] == lst[temp[0][0]][temp[0][1]]:
                temp.append((r,c))
    return min([lst[temp[0][0]][temp[0][1]] + min_total(making_list(lst, (r, c))) for r, c in temp])


def making_list(lst, rc):
    length = len(lst)
    if 0 < rc[1] < length - 1:
        return [lst[i][0:rc[1]] + lst[i][rc[1] + 1:length] for i in list(range(0, rc[0])) + list(range(rc[0] + 1, length))]

    elif rc[1] == 0:
        return [lst[i][rc[1] + 1:length] for i in list(range(0, rc[0])) + list(range(rc[0] + 1, length))]

    else:
        return [lst[i][0:rc[1]] for i in list(range(0, rc[0])) + list(range(rc[0] + 1, length))]




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, min_total(lst)))
