import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, *M = list(map(int, input().split()))

    # 도착 가능한 정류장의 인덱스-1 저장 (0부터 시작)
    reach = [0] * (N-1)
    for idx, charger in enumerate(M):
        reach[idx] = idx + charger

    cnt = 0
    dest = N-1
    while dest:
        for i in range(N-1):
            if reach[i] >= dest:
                cnt += 1
                dest = i
                break

    print('#{} {}'.format(tc, cnt-1))