import sys
sys.stdin = open('input.txt')
for tc in range(1,11):
    case = int(input())
    list_b= list(map(int,input().split()))
    for c in range(case):
        list_b[list_b.index(max(list_b))]-=1
        list_b[list_b.index(min(list_b))]+=1
    print("#{} {}".format(tc, max(list_b)-min(list_b)))