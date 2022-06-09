import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    se_list=[]
    c_list=[0]*5001
    for _ in range(N):
        se_list.append(list(map(int, input().split())))

    for i in se_list:
        for j in range(i[0], i[1]+1):
                c_list[j]+=1
    P = int(input())
    bus_stop=[]
    for _ in range(P):
        bus_stop.append(c_list[int(input())])

    print("#{}".format(tc), ' '.join(map(str, bus_stop)))