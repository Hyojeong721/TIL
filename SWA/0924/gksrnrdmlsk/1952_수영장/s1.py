# 1953.[모의 SW 역량테스트] 탈주범 검거
# 1952.[모의 SW 역량테스트] 수영장
# 1949.[모의 SW 역량테스트] 등산로 조성

# 완전탐색
import sys
import itertools
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    d, m, tr, y = map(int, input().split())
    bp = m // d + 1
    lst = [0] + list(map(int, input().split()))
    for idx, value in enumerate(lst):
        if value >= bp:
            lst[idx] = m
        else:
            lst[idx] = d * value

    three_m = [(i, i + 2) for i in range(1, 11)] # 3달권의 경우의 수

    plan_1 = min([sum(lst) - lst[i[0][0]] - lst[i[0][0] + 1] - lst[i[0][1]] + tr for i in list(itertools.combinations(three_m, 1))])
    plan_2 = 36000
    for i in itertools.combinations(three_m, 2):
        temp_set = set(range(i[0][0], i[0][1] + 1)) | set(range(i[1][0], i[1][1] + 1))
        if plan_2 > sum(lst) - sum([lst[i] for i in temp_set]) + tr * 2:
            plan_2 = sum(lst) - sum([lst[i] for i in temp_set]) + tr * 2

    plan_3 = 36000
    for i in itertools.combinations(three_m, 3):
        temp_set = (set(range(i[0][0], i[0][1] + 1)) | set(range(i[1][0], i[1][1] + 1))) | set(range(i[2][0], i[2][1] + 1))
        if plan_3 > sum(lst) - sum([lst[i] for i in temp_set]) + tr * 3:
            plan_3 = sum(lst) - sum([lst[i] for i in temp_set]) + tr * 3

    plan_4 = 4 * tr
    print('#{} {}'.format(tc, min(sum(lst), plan_1, plan_2, plan_3, plan_4, y)))