import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    stick = input()
    num_stick = 0       # 자를 수 있는 막대 수
    total_stick = 0     # 자르기 전 총 막대 수
    partition = 0       # 잘린 조각 수

    for idx, x in enumerate(stick):
        # ( : 새로운 막대 or 레이저 시작
        if x == '(':
            if stick[idx + 1] == '(':
                num_stick += 1
                total_stick += 1
            else:
                partition += num_stick

        # ) : 자르기 끝낸 막대 or 레이저 끝
        else:
            if stick[idx - 1] != '(':
                num_stick -= 1

    print('#{0} {1}'.format(tc, partition + total_stick))