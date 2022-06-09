import sys
sys.stdin = open("input.txt")
for tc in range(1,11):
    N =int(input())
    list_a=[]
    for _ in range(8):
        list_a.append(list(input()))
    count=0

    for x in range(8):
        for start_y in range(8-N+1):
            if list_a[x][start_y:start_y+N]==list(reversed(list_a[x][start_y:start_y + N])):
                count+=1

    for y in range(8):
        for start_x in range(8-N+1):
            strlist = []
            for idx in range(N):
                strlist.append(list_a[start_x+idx][y])
            if strlist==list(reversed(strlist)):
                count+=1


    print("#{} {}".format(tc, count))