import sys
sys.stdin =open('input.txt')

for tc in range(int(input())):
    size = int(input())
    count = 0
    list1=[[0]*size for _ in range(size)]
    print(list1)
    ni = 0
    nj = -1
    m=0
    while count <size**2:
        di = [0,1,0,-1] # 오른쪽 아래 왼쪽 위
        dj = [1,0,-1,0]
        if ni+di[m] in range(size) and nj+dj[m] in range(size) and list1[ni+di[m]][nj+dj[m]]==0: #한칸을 이동 했을 때 가능한가?
            ni, nj = ni+di[m], nj+dj[m] # 가능하다면 이동하고
            count += 1 # 1을 더해서
            list1[ni][nj] = count # 값을 넣어주기
        else:
            m=(m+1)%4 # 아니라면 꺾어야 하므로 m증가시키기

    print(list1)
