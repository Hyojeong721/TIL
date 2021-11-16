# swea 4834 숫자카드
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
import sys
sys.stdin = open('input.txt')

# 먼저, 테스트 케이스의 수를 받는다.
T = int(input())
for c in range(1, T+1):

    # 숫자 카드의 수 N
    N = int(input())
    # 카드의 리스트를 설정한다.
    cards = list(map(int, (input())))
    # 가장 많은 카드의 개수와 카드의 숫자 초기 설정한다.
    cnt_max = 0
    num_max = 0
    # 모든 카드에 대해서 다른 카드와 비교
    for i in range(N):
        # 비교하는 카드의 개수와 최대값을 비교하기 위한 cnt 변수를 설정하였다.
        cnt = 0
        # 비교했던 카드는 중복해서 비교할 필요 없기 때문에 제외하고 비교할 수 있도록 range 설정
        for j in range(i, N):
            # 같은 카드인 경우 cnt += 1 을 해준다.
            if cards[i] == cards[j]:
                cnt += 1
        # i 카드의 모든 다른 카드와 비교가 끝났을 때, 카드의 개수를 최대값과 비교한 후 cnt가 크거나 같으면 같은 값으로 설정한다.
        if cnt >= cnt_max:
            cnt_max = cnt
            # 최대개수 값으로 설정된 카드인 경우, 카드 자체의 숫자 크기를 최대 숫자크기값과 비교한다.
            if num_max <= cards[i]:
                num_max = cards[i]
# 출력
    print('#{} {} {}'.format(c, num_max, cnt_max))
