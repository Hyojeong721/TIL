import sys
sys.stdin = open('input.txt')

T = int(input())

N, M = map(int, input().split())

mat = [input() for _ in range(N)]
print(mat)


result = ''
for row in range(N):
    for col in range(N-M+1):
        if mat[row][col:col + M] == mat[row][col:col + M][::-1]:
            result = mat[row][col:col + M]
print(result)

...