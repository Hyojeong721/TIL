import sys
sys.stdin = open('input.txt')

# 재귀쓰
def rsp(lst):
    length = len(lst)
    if length == 2:
        if (lst[0][1] == 1 and lst[1][1] == 2) or (lst[0][1] == 2 and lst[1][1] == 3) or (
                lst[0][1] == 3 and lst[1][1] == 1):
            return lst[1]
        else:
            return lst[0]

    elif length == 3:
        return rsp([rsp(lst[0:2]), lst[2]])

    else:
        return rsp([rsp(lst[0: (length + 1) // 2])] + [rsp(lst[(length + 1) // 2: length])])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    temp_lst = list(map(int, input().split()))
    lst = []
    for i, j in enumerate(temp_lst):
        lst.append((i + 1, j))

    print('#{} {}'.format(tc, rsp(lst)[0]))

