N = 5

test = [[0]*N for _ in range(N)]
for k in range(N):
    print(*test[k])
print("===============")
def inToout():
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    loc = (N//2, N//2)
    test[loc[0]][loc[1]] = 0
    dist = 1
    cnt = 0
    dir = 0
    num = 1
    while True:
        for i in range(dist):
            if dist == N and i == dist - 1:
                break
            ni, nj = loc[0]+di[dir], loc[1]+dj[dir]
            loc = (ni, nj)
            test[ni][nj] = num
            num += 1


        cnt += 1
        dir = (dir+1) % 4
        if cnt == 2:
            cnt = 0
            dist += 1
        if dist == N and cnt == 1:
            break
inToout()



def outToin():
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    loc = (0, -1)
    dist = N
    dir = 0
    cnt = 1
    while True:
        for i in range(dist):
            ni = loc[0] + di[dir]
            nj = loc[1] + dj[dir]
            loc = (ni, nj)
            print(loc)
            test.append(num)
        cnt += 1
        dir = (dir + 1) % 4
        if cnt == 2:
            cnt = 0
            dist -= 1
        print(test)
        if dist == 0:
            break

for i in range(N):
    print(*test[i])