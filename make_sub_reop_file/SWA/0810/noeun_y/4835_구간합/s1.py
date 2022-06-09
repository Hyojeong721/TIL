import sys
sys.stdin = open('input.txt')
for tc in range(int(input())):
    size, num = map(int, input().split())
    numlist = (list(map(int, input().split())))

    for i in range(size - num + 1):
        ans = 0
        max = numlist[0]
        min = numlist[0]
        for j in range(num):
            ans += numlist[i + j]
        if max <= ans:
            max = ans

        elif min > ans:
            min = ans



    #print(f"#{tc + 1} {max - min}")




