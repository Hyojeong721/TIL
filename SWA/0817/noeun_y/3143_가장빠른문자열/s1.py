import sys
sys.stdin = open("input.txt")
for tc in range(1,int(input())+1):
    str1,key=input().split()
    count = str1.count(key)
    print("#{} {}".format(tc,count+ len(str1)-count*len(key)))