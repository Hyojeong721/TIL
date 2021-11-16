import sys
sys.stdin = open('input.txt')


def check_babygin(numbers):
    """
    주어진 숫자들로 babygin(run이나 triplet)이 되는지 여부를 판단한다.
    """
    # 카드의 개수가 3개 미만인 경우 => False를 리턴한다.
    if len(numbers) < 3:
        return False

    # counts: 각 숫자의 개수를 담은 배열 (ex. counts[3] = 2면, 3이 2개)
    counts = [0] * 10
    for num in numbers:
        counts[num] += 1

    # 1. triplet 검사 (같은 숫자가 3개 이상)
    if max(counts) >= 3:
        return True

    # 2. run 검사 (연속된 숫자 3개)
    for i in range(8):
        if counts[i] and counts[i + 1] and counts[i + 2]:
            return True

    return False


T = int(input())

for tc in range(1, T + 1):
    numbers = [int(x) for x in input().split()]
    player1 = []
    player2 = []
    winner = 0

    for i in range(12):
        if i % 2 == 0:
            player1.append(numbers[i])

            if check_babygin(player1):
                winner = 1
                break
        else:
            player2.append(numbers[i])

            if check_babygin(player2):
                winner = 2
                break

    print("#{} {}".format(tc, winner))
