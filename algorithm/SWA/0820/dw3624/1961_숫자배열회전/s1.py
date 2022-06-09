import sys
sys.stdin = open('input.txt')

T = int(input())

def rotate(mat):
    global n
    tmp = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            tmp[row][col] = mat[(n-1)-col][row]
    return tmp


for t in range(1, T+1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    m090 = rotate(mat)
    m180 = rotate(m090)
    m270 = rotate(m180)

    print('#{}'.format(t))
    for row in range(n):
        tmp1 = tmp2 = tmp3 = ''

        for col in range(n):
            tmp1 += str(m090[row][col])
        for col in range(n):
            tmp2 += str(m180[row][col])
        for col in range(n):
            tmp3 += str(m270[row][col])

        print('{} {} {}'.format(tmp1, tmp2, tmp3))