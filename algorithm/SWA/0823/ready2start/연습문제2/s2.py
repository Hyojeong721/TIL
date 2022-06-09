data = [*range(1, 11)]
N = len(data)
selected = [0] * N


def powerset(idx, total):
    """
    Args:
        idx: 현재 탐색 중인 인덱스
        total: 현재까지의 부분집합의 합
    """
    # 전체 길이를 다 확인한 경우 => 탐색 종료
    if idx == N:
        return

    # 현재까지의 부분집합의 합이 10보다 큰 경우 => 탐색 종료
    if total > 10:
        return

    # 현재까지의 부분집합의 합이 10인 경우 => 합이 10인 부분집합 발견!
    if total == 10:
        for i in range(N):
            if selected[i] == 1:
                print(data[i], end=" ")
        print()
        return

    selected[idx] = 1
    powerset(idx + 1, total + data[idx])
    selected[idx] = 0
    powerset(idx + 1, total)


powerset(0, 0)
