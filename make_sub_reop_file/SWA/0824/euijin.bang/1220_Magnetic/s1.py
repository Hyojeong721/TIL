import sys
sys.stdin = open("input.txt")

# 90도 오른쪽으로 회전한 2차원 배열
N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]

rotated_arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        rotated_arr[j][N-1-i] = input_arr[i][j]

print(rotated_arr)

cnt = 0

for i in range(N):
    hasOne = False
    hasTwo = False
    for j in range(N):
        if rotated_arr[i][j] == 2:
            hasTwo = True
        if hasTwo and rotated_arr[i][j] == 1:
            hasOne = True
        if hasOne and hasTwo:
            cnt += 1
            hasOne = False
            hasTwo = False
print(cnt)


# 다른 방법도!











