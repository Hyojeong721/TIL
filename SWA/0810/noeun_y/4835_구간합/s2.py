import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    size, num = map(int, input().split())
    numlist = (list(map(int, input().split())))
    ans = 0
    max_n = sum(numlist[0:num])
    min_n = sum(numlist[0:num])
    #print(max_n)
    for i in range(size - num + 1):
        ans=sum(numlist[i:i+num])
        # for j in range(num):
        #     ans += numlist[i + j]
        if max_n <= ans:
            max_n = ans
        elif min_n > ans:
            min_n = ans
    print(max_n-min_n)
