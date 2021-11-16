import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards_list = input()

    # 카드를 각각 분리
    cards = []
    for i in cards_list:
        cards.append(int(i))

    # 인덱스 숫자에 해당하는 값에 등장 횟수 +1
    result_list = [0] * 10
    for i in cards:
        result_list[i] += 1

    # 등장횟수(value)가 가장 많은 인덱스 번호(maxV)와 값(max_num) 출력
    max_num = 0
    max_V = 0
    for i in range(len(result_list)):
        if max_num <= result_list[i]:
            max_num = result_list[i]
            max_V = i
    print('#{} {} {}'.format(tc, max_V, max_num))