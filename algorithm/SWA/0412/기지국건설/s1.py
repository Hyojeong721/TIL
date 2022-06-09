import sys
sys.stdin = open("test.txt")

t = int(input())
for tc in range(1, t+1):
    answer = 0
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    ex = [(-1,0),(0,-1),(1,0),(0,0),(-1,1),(0,1),(1,1)]
    for x in range(w):
        for y in range(h):
            temp = []

            for m in ex:
                nx = x + m[0]
                ny = y + m[1]

                if 0 <= nx < w and 0 <= ny < h:
                    temp.append([nx, ny, arr[ny][nx]])

            if len(temp) >= 4:
                temp_answer = temp[0][2]
                temp.sort(key=lambda x: x[2], reverse=True)
                res = [(temp[0][0], temp[0][1])]
                idx = 1
                cnt = [(temp[0][0], temp[0][1])]
                while idx < len(temp):
                    if len(cnt) == 4:
                        break
                    test_x = temp[idx][0]
                    test_y = temp[idx][1]
                    test_res = temp[idx][2]
                    for m in ex:
                        if (test_x+m[0], test_y+m[1]) in res and (test_x+m[0], test_y+m[1]) not in cnt:
                            temp_answer += test_res
                            cnt.append((test_x+m[0], test_y+m[1]))
                            print(temp[idx])
                            break

                    idx += 1
            answer = max(answer, temp_answer)

    print("#{} {}".format(tc, answer**2))