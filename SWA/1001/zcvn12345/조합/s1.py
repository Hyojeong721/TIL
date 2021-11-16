# for i in range(8):
#     for j in range(i+1, 9):
#         for k in range(j+1, 10):
#             print(i, j, k)
#
def nCr(n, r, s, k):
    if k == r:
        print(comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(n, r, i+1, k+1)

N = 10
R = 3
comb = [0]*R
nCr(N, R, 0, 0)