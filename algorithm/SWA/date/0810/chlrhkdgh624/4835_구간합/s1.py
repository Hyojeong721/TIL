import sys
sys.stdin = open('input.txt')
T = int(input())

N = []
M = []
V = []


for i in range(T):
    NM = list(map(int, input().split()))
    N.append(NM[0])
    M.append(NM[1])
    V.append(list(map(int, input().split())))

for i in range(T):
    maximum = 0
    minimum = 0
    for j in range(0, N[i] - M[i] + 1):
        num = sum(V[i][j:j+M[i]])
        if num > maximum:
            maximum = num

        if j == 0:
            minimum = num

        if num < minimum:
            minimum = num

    print(f'#{i+1} {maximum - minimum}')
