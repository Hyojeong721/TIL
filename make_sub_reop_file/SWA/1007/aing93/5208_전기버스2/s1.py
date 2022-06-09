import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    inputlist=list(map(int,input().split()))
    N = inputlist[0]
    bs = inputlist[1:]
    stop = 0
    nsum=bs[0]
    cnt=0

    while stop <len(bs):
        cnt+=1
        max = 0

        if stop+bs[stop]>=len(bs):
            break
        for i in range(stop,stop+bs[stop]+1):
            if max < i+bs[i]:
                max = i+bs[i]
                stop = i


    print("#{} {}".format(tc,cnt-1))