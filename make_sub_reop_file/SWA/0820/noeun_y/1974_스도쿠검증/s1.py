import sys
sys.stdin= open("input.txt")

for tc in range(1,int(input())+1):
    s_list=[]
    result=1
    for _ in range(9):
        s_list.append(list(map(int,input().split())))

    for i in range(9):
        if len(set(s_list[i]))!=9:
            result=0
            break
        check_list=[]
        for j in range(9):
            check_list.append(s_list[j][i])
        if len(set(check_list))!=9:

            result=0
            break


    for i in range(3):
        for j in range(3):
            check_list = []
            first_i = 3*i
            first_j = 3*j
            for x in range(3):
                check_list.extend(s_list[first_i+x][first_j:first_j+3])
            if len(set(check_list))!=9:

                result=0
                break

    print("#{} {}".format(tc,result))
