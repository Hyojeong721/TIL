import sys
sys.stdin = open('input.txt')


def get_most_frequent(numbers):
    """
    0~9 중 가장 많은 카드에 적힌 숫자와 개수를 반환한다.
    numbers: 카드 숫자 목록 (str)  ex. '48295'

    counts: 카드에 적힌 숫자의 개수 (배열)
            (counts[i] : 숫자 i의 개수)
    max_num: 가장 많은 카드에 적힌 숫자
    """
    counts = [0] * 10
    max_num = 0

    for number in numbers:
        counts[int(number)] += 1

    for i in range(10):
        # 카드 장수가 같을 때는 숫자가 큰 쪽을 저장
        if counts[max_num] <= counts[i]:
            max_num = i

    return max_num, counts[max_num]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()

    max_number, max_count = get_most_frequent(cards)
    print("#{} {} {}".format(tc, max_number, max_count))
