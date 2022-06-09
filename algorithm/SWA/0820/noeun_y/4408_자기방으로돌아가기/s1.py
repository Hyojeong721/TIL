import sys
sys.stdin= open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    room=[0]*401
    n_list=[]
    for _ in range(N):
        a,b = map(int,input().split())

        if a>b:
            a,b=b,a
        if b%2!=0:
            b+=1

        for i in range(a,b+1):
            room[i]+=1


    #print(room)
    print("#{} {}".format(tc, max(room)))
