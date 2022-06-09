import sys
sys.stdin = open('input.txt')

def setIsSel(pos):
    val = lst[pos]
    isSel[pos] = 2

    pos -= 1
    while pos >= 0 and lst[pos] < val:
        isSel[pos] = 1
        pos -= 1


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    isSel = [0] * n
    for i in range(1, n):
        if lst[i-1] < lst[i]:
            setIsSel(i)

    profit = 0
    cnt = 0
    for i in range(n):
        if isSel[i] == 1:
            profit -= 1
            cnt += 1
        elif isSel[i] == 2:
            profit += lst[i] * cnt - sum(lst[i-cnt:i])
            cnt = 0

    print('#{} {}'.format(tc, profit))

    # print(profit)