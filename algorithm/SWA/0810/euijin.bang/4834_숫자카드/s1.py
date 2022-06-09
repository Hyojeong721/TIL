import sys
sys.stdin = open('input.txt')

T = int(input())

# N = 주어진 카드의 숫자
# Card = 주어진 카드의 리스트
# Counts = 카드 횟수를 셀 리스트

# 카드 장수가 같으면 적힌 쪽이 큰 숫자를 출력!! - enumerate를 쓰는 이유

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    counts = [0] * 10

    # counts 의 인덱스에 맞추어 카드 장수를 세어 넣는다.
    for i in range(N):
        counts[cards[i]] += 1

    temp_max = 0 # 가장 많이 나온 횟수를 저장
    temp_idx = 0 # 가장 많이 나온 숫자를 저장

    for idx, value in enumerate(counts):
        if value > temp_max:
            temp_max = value
            temp_idx = idx
        elif value == temp_max:
            if idx > temp_idx:
                temp_idx = idx

    print("#{} {} {}".format(tc, temp_idx, temp_max))