import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    timetable = []

    for _ in range(N):
        start, end = map(int, input().split())
        timetable.append((start, end))

    # 그리디: 도착 시간이 빠른 시간부터 시간표를 이어붙인다.
    timetable.sort(key=lambda x: x[1])
    current, count = 0, 0

    for start, end in timetable:
        if current <= start:
            count += 1
            current = end

    print("#{} {}".format(tc, count))
