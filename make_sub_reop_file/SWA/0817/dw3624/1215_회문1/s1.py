import sys
sys.stdin = open('input.txt')

T = 10

def pal_cnt(mat):
    cnt = 0
    for row in mat:
        # print(row)
        if n % 2:
            for i in range(n//2, len(row)+1):
                temp1 = row[i-n//2:i]
                temp2 = row[i+1:i+n//2+1][::-1]
                # print(i, temp1, temp2, end = ' ')
                if temp1 == temp2:
                    cnt += 1
            # print()
        else:
            for i in range(n//2, len(row)+1):
                temp1 = row[i-n//2:i]
                temp2 = row[i:i+n//2][::-1]
                if temp1 == temp2:
                    cnt += 1
    return cnt

for t in range(1, T + 1):
    n = int(input())
    mat = [input() for _ in range(8)]
    mat_t = []
    for col in range(len(mat)):
        tmp = ''
        for row in range(len(mat)):
            tmp += mat[row][col]
        mat_t.append(tmp)

    a1 = pal_cnt(mat)
    a2 = pal_cnt(mat_t)
    result = a1 + a2

    print('#{} {}'.format(t, result))