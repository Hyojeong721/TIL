import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    case = int(input())
    list1= list(map(int,input().split()))
    #print(list1)
    count = 0
    for i in range(2,len(list1)-2):
        maxh=max(list1[i-2], list1[i-1], list1[i+1], list1[i+2])
        if list1[i]> maxh:
            count+=list1[i]-maxh
    print("#{} {}".format(tc,count))