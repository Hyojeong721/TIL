import sys
sys.stdin = open("input.txt")

def plus(c_paper,x):
    global count, floor,result
    if c_paper==floor:
        count+=x
    if c_paper<floor:
        plus(c_paper+10,x*1)
        plus(c_paper+20,x*2)


for tc in range(1,int(input())+1):
    # 경우가 2개 뿐 1,2
    floor=int(input())
    result=1
    c_paper=0
    count =0
    plus(0,1)
    print("#{} {}".format(tc,count))

