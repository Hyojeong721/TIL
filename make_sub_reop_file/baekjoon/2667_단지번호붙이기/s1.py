import sys
sys.stdin = open('test.txt')

def check(i, j, cnt):
    global arr
    dici = [-1, 1, 0, 0]
    dicj = [0, 0, -1, 1]
    arr[i][j] = cnt

    for k in range(4):
        ni = i + dici[k]
        nj = j + dicj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] == 1:
                check(ni, nj, cnt)

    return

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
cnt = 2
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            check(i, j, cnt)
            cnt += 1
print(cnt-2)
answer = [0 for i in range(cnt)]
for row in range(n):
    for c in range(2, cnt):
        answer[c] += arr[row].count(c)

answer.sort()

for ans in answer[2:]:
    print(ans)

