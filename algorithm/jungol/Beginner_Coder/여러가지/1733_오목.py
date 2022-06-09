arr = []
for i in range(19):
    arr.append(list(map(int, input().split())))
def search(y, x, c):
    # 상
    if 0 <= y-4 and arr[y-4][x] == c:
        for i in range(1, 4):
            if arr[y-i][x] != c:
                return [False]
        return [True, y-5, x, y-4, x]

    # 하
    elif y + 4 < 19 and arr[y+4][x] == c:
        for i in range(1, 4):
            if arr[y+i][x] != c:
                return [False]
        return [True, y+5, x, y+4, x]

    # 좌
    elif 0 <= x-4 and arr[y][x-4]==c:
        for i in range(1, 4):
            if arr[y][x-i] != c:
                return [False]
        return [True, y, x-5, y, x-4]
    # 우
    elif x + 4 < 19 and arr[y][x+4] == c:
        for i in range(1, 4):
            if arr[y][x+i] != c:
                return [False]
        return [True, y, x+5, y, x+4]
    # 11시
    elif 0 <= x-4 and 0 <= y-4 and arr[y-4][x-4] == c:
        for i in range(1, 4):
            if arr[y-i][x-i] != c:
                return [False]
        return [True, y-5, x-5, y-4, x-4]

    # 2시
    elif x + 4 < 19 and 0 <= y - 4 and arr[y - 4][x + 4] == c:
        for i in range(1, 4):
            if arr[y - i][x + i] != c:
                return [False]
        return [True, y-5, x+5, y-4, x+4]

    # 7시
    elif 0 <= x - 4 and y + 4 < 19 and arr[y + 4][x - 4] == c:
        for i in range(1, 4):
            if arr[y + i][x - i] != c:
                return [False]
        return [True, y+5, x-5, y+4, x-4]
    # 5시
    elif x + 4 < 19 and y + 4 < 19 and arr[y + 4][x + 4] == c:
        for i in range(1, 4):
            if arr[y + i][x + i] != c:
                return [False]
        return [True, y+5, x+5, y+4, x+4]

    return [False, y, x]

for i in range(19):
    for j in range(19):
        if arr[i][j]:
            res = search(i, j, 1)
            print(res)
            if res[0]:
                if 0 <= res[1] < 19 and 0 <= res[2] < 19:
                    if arr[res[1]][res[2]] != 1:
                        print(1)
                        print(res[3], res[4])
                    else:
                        continue
                else:
                    print(1)
                    print(res[3], res[4])
        elif arr[i][j] == 2:
            res = search(i, j, 2)
            print(res)
            if res[0]:
                if 0 <= res[1] < 19 and 0 <= res[2] < 19:
                    if arr[res[1]][res[2]] != 2:
                        print(2)
                        print(res[3], res[4])
                    else:
                        continue
                else:
                    print(1)
                    print(res[3], res[4])


