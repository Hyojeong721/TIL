import sys
sys.stdin =open('input.txt')

for tc in range(1,int(input())+1):
    list_n =list(map(int,input().split()))
    #print(list_n)

    count=0
    for i in range(1<<len(list_n)):
        result = 0
        for j in range(len(list_n)):
            if i & (1<<j):
                result+=list_n[j]
        #print(result)

        if result==0:

            count+=1
    if count>1:

        print("#{} 1".format(tc))
    else:

        print("#{} 0".format(tc))

