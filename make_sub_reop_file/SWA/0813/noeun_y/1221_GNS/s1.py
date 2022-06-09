import sys
sys.stdin = open("input.txt")

for _ in range(int(input())):
    N,num =(input().split())

    list_n = (input().split())
    list_num=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    list_num_c=[0,0,0,0,0,0,0,0,0,0]

    for n in range(len(list_num)):
        for i in list_n:
            if i ==list_num[n]:
                list_num_c[n]+=1

    print(N)
    for i in range(len(list_num)):
        print((list_num[i]+" ")*list_num_c[i],end="")

    print("")