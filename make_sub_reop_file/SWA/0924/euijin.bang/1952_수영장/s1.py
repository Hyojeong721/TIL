import sys
sys.stdin = open("sample_input.txt")
from itertools import combinations

T = int(input())
for tc in range(T):
    day, month, three_months, year = map(int, input().split()) # 각 이용권 요금
    monthly_plan = list(map(int, input().split())) # 이용 계획


    # 모두 1일권으로 이용시
    day_only_fee = sum(monthly_plan) * day


    # 모두 1달권으로 이용시
    month_count = 0 # 1회 이상 이용한 달의 수
    for i in range(12):
        if monthly_plan[i] != 0:
            month_count += 1
    month_only_fee = month_count * month


    use_list = [] # 1회 이상 이용한 달만 모은 리스트 [2, 9, 1, 5]
    for plan in monthly_plan:
        if plan != 0:
            use_list.append(plan)

    # 일일권과 한달권 섞어서 이용시
    mix_fee_list = []
    for i in range(1, len(use_list)): # 1 2 3 4  # 1, 3  / 2, 2 / 3, 1
        day_use = i
        month_use = len(use_list) - day_use
        perm = list(combinations(use_list, day_use))
        for j in range(len(perm)):
            mix_fee = sum(perm[j]) * day + month_use * month
            mix_fee_list.append(mix_fee)


    # 일일권과 세달권 섞어서 이용시
    for i in range(1, len(use_list)):  # 1 2 3 4  # 1, 3  / 2, 2 / 3, 1
        if len(use_list) >= 9:
            for k in range(1, 3):
                day_use = len(use_list) - 3
                perm = list(combinations(use_list, day_use))
                for j in range(len(perm)):
                    mix_fee = sum(perm[j]) * day + three_months * 3
                    mix_fee_list.append(mix_fee)

        elif len(use_list) >= 6:
            for k in range(1, 3):
                day_use = len(use_list) - 2
                perm = list(combinations(use_list, day_use))
                for j in range(len(perm)):
                    mix_fee = sum(perm[j]) * day + three_months * 2
                    mix_fee_list.append(mix_fee)

        elif len(use_list) >= 3:
            for k in range(1, 3):
                day_use = len(use_list) - 1
                perm = list(combinations(use_list, day_use))
                for j in range(len(perm)):
                    mix_fee = sum(perm[j]) * day + three_months * 1
                    mix_fee_list.append(mix_fee)

    # 한달권과 세달권 섞어서 이용시
    for i in range(1, len(use_list)):  # 1 2 3 4  # 1, 3  / 2, 2 / 3, 1
        if len(use_list) >= 9:
            month_use = len(use_list) - 3
            mix_fee = month * month_use + three_months * 3
            mix_fee_list.append(mix_fee)

        elif len(use_list) >= 6:
            month_use = len(use_list) - 2
            mix_fee = month * month_use + three_months * 2
            mix_fee_list.append(mix_fee)

        elif len(use_list) >= 3:
            month_use = len(use_list) - 1
            mix_fee = month * month_use + three_months * 1
            mix_fee_list.append(mix_fee)



    # 1년 이용권 이용시
    year_fee = year

    total_fee_list = []
    # 총 리스트
    total_fee_list.append(day_only_fee)
    total_fee_list.append(month_only_fee)
    total_fee_list.extend(mix_fee_list)
    total_fee_list.append(year_fee)
    result = min(total_fee_list)

    print('#{} {}'.format(tc + 1, result))