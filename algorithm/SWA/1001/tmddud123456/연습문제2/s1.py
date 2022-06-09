def perm(babygin, k):
    global N, used, total, temp
    if k == N:
        total.append(temp)
    else:
        for i in range(N):
            if used[i] == 0:
                temp += babygin[i]
                used[i] = 1
                perm(babygin, k+1)
                temp = temp[:-1]
                used[i] = 0

def babyGin(total):
    for i in range(len(total)):
        if int(total[i][0]) == int(total[i][1]) == int(total[i][2]) or int(total[i][0]) == int(total[i][1]) +1 == int(total[i][2])+2:
            if int(total[i][3]) == int(total[i][4]) == int(total[i][5]) or int(total[i][3]) == int(total[i][4]) +1 == int(total[i][5])+2:
                return 'baby-gin'
    return 'not baby-gin'


A = '101123'
N = len(A)
used = [0]*N
total = []
temp = ''
perm(A, 0)
print(total)
print(babyGin(total))