import sys
sys.stdin = open("input.txt")

for tc in range(10):
    N=int(input())
    findstr=input()
    str1=input()
    count=0
    #print(findstr)
    for i in range(len(str1)-len(findstr)+1):
        if str1[i:i+len(findstr)]==findstr:
            count+=1
    print("#{} {}".format(N,count))
