import sys
sys.stdin = open('input.txt')
case = int(input())

for tc in range(case):
    size = int(input())
    num = list(input())  # 그냥 리스트로 받으면 문자형으로 하나하나 리스트에 들어간다.
    countlist = [0] * 10
    count = 0
    ans = 0
    ind = 0
    for i in num:
        count = int(i)
        countlist[count] = countlist[count] + 1

    res = 0
    for idx, value in enumerate(countlist):
        if ans <= value:
            ans = value
            res = idx

    print(f'#{tc + 1} {res} {ans}')

