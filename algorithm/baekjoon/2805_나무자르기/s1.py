import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = min(trees), max(trees)

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in trees:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
