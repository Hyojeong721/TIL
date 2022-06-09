import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    """
    numbers: 입력받은 숫자 배열
    n: numbers의 길이
    count: 총합이 0인 부분 집합의 개수
    sum_zero: 공집합을 제외하고 총합이 0인 부분 집합이 있는지의 여부
              (있다면 True, 없다면 False)
    """
    numbers = list(map(int, input().split()))
    n = len(numbers)
    # 원소가 하나도 없는 집합은 제외해야 하므로, count의 초기값을 -1로 설정한다.
    count = -1
    sum_zero = False

    for i in range(1 << n):
        total = 0
        for j in range(n):
            if i & (1 << j):  # i의 j번째 비트가 1이라면 numbers[j]을 더한다.
                total += numbers[j]

        # 부분 집합의 총합이 0이라면
        if not total:
            count += 1
            # 총합이 0인 부분 집합의 개수가 2개 이상이라면
            # 총합이 0인 부분 집합이 있음을 확인했으므로 탐색을 종료한다.
            if count > 0:
                sum_zero = True
                break

    print("#{} {}".format(tc, int(sum_zero)))
