import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    array = list(map(int, input()))

    cnt = [0] * 10 # 카드 최대 숫자 + 1
    max_cnt = 0 # 가장 많은 카드 장수!
    max_card = 0 # 가장 많은 카드의 숫자
    for i in range(N):
        cnt[array[i]] += 1
        if max_cnt < cnt[array[i]]:
            max_cnt = cnt[array[i]]
            max_card = array[i]
        elif max_cnt == cnt[array[i]]:
            if max_card < array[i]:
                max_cnt = cnt[array[i]]
                max_card = array[i]

    print('#{} {} {}'.format((test_case),  max_card, max_cnt))
