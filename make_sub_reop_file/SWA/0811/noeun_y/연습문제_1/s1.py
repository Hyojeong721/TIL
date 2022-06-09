import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    list_p=[]
    for _ in range(int(input())):
        list_p.append(list(map(int, input().split())))
    result =0
    for i in range(len(list_p)):
        for j in range(len(list_p[0])):
            for m in range(4):
                dx=[0,0,-1,1]
                dy=[1,-1,0,0]
                if i+dx[m] in range(len(list_p)) and j+dy[m] in range(len(list_p)):
                    #print(i+dx[m],j+dy[m])
                    result += abs(list_p[i][j]-list_p[i+dx[m]][j+dy[m]])

    print("#{} {}".format(tc, result))