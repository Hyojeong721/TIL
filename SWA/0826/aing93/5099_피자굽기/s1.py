import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    oven, pizza = map(int, input().split())
    cheese = list(map(int, input().split()))
    # 피자 순서 인덱스 만들어줌
    number = [i+1 for i in range(pizza)]
    # 오븐에 들어있는 피자와 밖에 있는 피자 구분
    inoven = cheese[0:oven]
    innumber = number[0:oven]
    leftpizza = cheese[oven:]
    leftnumber = number[oven:]
    while len(inoven) != 1:
        inoven[0] = inoven[0] // 2
        if inoven[0] == 0:
            inoven.pop(0)
            innumber.pop(0)
            if len(leftpizza) > 0:
                inoven.append(leftpizza[0])
                leftpizza.pop(0)
                innumber.append(leftnumber[0])
                leftnumber.pop(0)
        else:
            inoven.append(inoven.pop(0))
            innumber.append(innumber.pop(0))

    print('#{} {}'.format(tc, innumber[0]))
