'''

Fail(제한시간 초과)

레이저를 a로 바꾸는 과정이 막대가 커졌을 때 오래 걸려서 그런 것 같다.
(사실 잘 모름 ㅎㅎ)

'''

import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    stick = input()
    stick = stick.replace('()', 'a')
    # a(((aa)(a)a))(a)
    # (((a(aa))(a)a))(aa)

    # [막대기 열려있으면 1, a(레이저) 개수] * 총 막대기 개수
    cnt_lst = [[0, 0] for _ in range(stick.count('('))]
    cnt = 0
    for x in stick:
        if x == '(':
            cnt_lst[cnt][0] += 1
            cnt += 1

        elif x == 'a':
            # 열린 막대기의 레이저 개수 + 1
            for lst in cnt_lst:
                if lst[0]:
                    lst[1] += 1

        # 최근 열린 막대기부터 닫는다.
        elif x == ')':
            for lst in cnt_lst[::-1]:
                if lst[0]:
                    lst[0] -= 1
                    break
    partition = 0
    for lst in cnt_lst:
        if lst[1]:
            partition += lst[1] + 1

    print('#{0} {1}'.format(tc, partition))