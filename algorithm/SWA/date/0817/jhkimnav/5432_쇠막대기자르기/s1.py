import sys
sys.stdin = open('input.txt')


T = int(input())

for TC in range(1, T+1):
    answer = 0
    pre_stick_cnt = 0
    total_stick_cnt = 0
    str = input()

    i = 0
    while i < len(str):
        # 레이저 인지 판단
        if i < len(str)-2 and str[i:i+2] == '()':
            # 총 막대 갯수를 현재 쇠 막대 갯수만큼 추가
            total_stick_cnt += pre_stick_cnt
            # 레이저 이후로 검사하게끔 인덱스 증가
            i += 1
        # 막대기 추가
        elif str[i] == '(':
            pre_stick_cnt += 1
            total_stick_cnt += 1
        # 막대기 제거
        elif str[i] == ')':
            pre_stick_cnt -= 1
        i += 1
    answer = total_stick_cnt
    print('#{} {}'.format(TC, answer))