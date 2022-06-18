import sys
sys.stdin = open('input.txt')
for i in range(int(input())):
    n=int(input())
    list1=list(map(int,input().split( )))
    maxn = list1[0]
    minn = list1[0]
    for num in list1:

        if num >maxn:
            maxn=num
        if num < minn:
            minn=num
    print('#{0} {1}'.format(i+1,maxn-minn))
