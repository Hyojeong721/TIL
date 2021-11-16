import sys
sys.stdin = open("input.txt")
for tc in range(1,int(input())+1):
    str1 = input()
    str2 = input()
    result=0
    for i in str1:
        count=0
        count=str2.count(i)
        result= max(result,count)
    print("#{} {}".format(tc,result))