import sys
sys.stdin = open("input.txt")
for tc in range(1,int(input())+1):
    list_t=[]
    list_t=list(input())
    print(list_t)

    bar=0
    cut=0
    deep=0
    for i in range(len(list_t)):
        if list_t[i] =="(":
            if list_t[i+1]==")":
                #print(deep)
                cut+=deep
            else:
                bar+=1
                deep+=1
        elif list_t[i-1] !="(":
            deep-=1

    print("#{} {}".format(tc, cut + bar))