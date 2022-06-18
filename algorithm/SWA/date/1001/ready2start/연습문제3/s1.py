


def get_subsets_by_total(numbers, total):
    """
    정수 집합 numbers에 대하여, 원소의 합이 total인 모든 부분 집합을 구한다.
    """
    N = len(numbers)

    # total이 0인 경우, 빈 집합을 출력한다.
    if not total:
        print('{}')

    # 공집합을 제외한 모든 부분 집합에 대하여, 합이 total인지 검사한다.
    for i in range(1, 1 << N):
        subset = set()
        for j in range(N):
            if i & (1 << j):
                subset.add(numbers[j])

        # subset의 원소의 합이 total이라면, 집합을 출력한다.
        if sum(subset) == total:
            print(subset)


numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
get_subsets_by_total(numbers, 0)
