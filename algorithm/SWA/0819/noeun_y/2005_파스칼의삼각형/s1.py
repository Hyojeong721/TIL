import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    refloor=[]
    floor=[1]

    print("#{}".format(tc))
    print(1)
    for i in range(N-1):
        refloor.append(1)

        for num in range(len(floor)-1):
            refloor.append(floor[num]+floor[num+1])

        refloor.append(1)
        floor = refloor

        print(" ".join(str(i) for i in refloor))
        refloor=[]

