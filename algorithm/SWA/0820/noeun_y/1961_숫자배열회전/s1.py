import sys
sys.stdin= open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    num_list = []
    for _ in range(N):
        num_list.append(list(map(int, input().split())))

    print("#{}".format(tc))

    for i in range(N):
        for j in range(N):
            print(num_list[N-1-j][i],end="")
        print(" ",end="")
        for j in range(N):
            print(num_list[N-1-i][N-1-j],end="")
        print(" ",end="")
        for j in range(N):
            print(num_list[j][N-1-i],end="")
        print("")
