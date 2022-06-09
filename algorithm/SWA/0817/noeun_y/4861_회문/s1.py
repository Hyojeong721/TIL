import sys
sys.stdin = open("input.txt")
for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    list_a=[]
    for _ in range(N):
        list_a.append(list(input()))

    for start_x in range(N):
        for start_y in range(N-M+1):
            for idx in range(M//2):
                if list_a[start_x][start_y+idx]!=list_a[start_x][start_y+M-1-idx]:
                    break
            else:
                print("#{} ".format(tc), end="")
                for idx in range(M):
                    print(list_a[start_x][start_y+idx],end="")
                print("")
    for start_x in range(N-M+1):
        for start_y in range(N):
            for idx in range(M//2):
                if list_a[start_x+idx][start_y]!=list_a[start_x+M-1-idx][start_y]:
                    break
            else:
                print("#{} ".format(tc), end="")
                for idx in range(M):
                    print(list_a[start_x+idx][start_y],end="")
                print("")