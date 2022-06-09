import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    list_t = [list(map(int,input().split())) for _ in range(N)]

    # 가능한 부분 1
    # 오른쪽으로 가능한 경우
    result=0
    for i in range(N):
        count = 0
        for j in range(N):

            if list_t[i][j]==1: # 1을 찾았다면 카운트 시작
                count+=1
            else:
                if count==K:
                    result+=1
                count=0
        if count == K:
            result += 1

    for i in range(N):
        count = 0
        for j in range(N):

            if list_t[j][i]==1: # 1을 찾았다면 카운트 시작
                count+=1
            else:
                if count==K:
                    result+=1
                count=0
        if count == K:
            result += 1




    print("#{} {}".format(tc,result))

    # 왼쪽으로 가능한 경