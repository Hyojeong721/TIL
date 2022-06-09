import sys
sys.stdin= open("input.txt")

for tc in range(1,int(input())+1):

    list_str=[[] for _ in range(16)]
    for _ in range(5):
        str1 = input()
        for i in range(len(str1)):
            list_str[i].append(str1[i])

    print("#{}".format(tc),end=" ")
    for i in list_str:
        for j in i:
            print(j,end="")
    print("")

