import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = list(input())
    lasers = [] # 레이저 위치입니다.
    for i in range(len(lst) - 1):
        if lst[i] + lst[i + 1] == '()':
            lasers.append(i)

    sticks = [] # 쇠막대기의 시작과 끝점 튜플을 원소로 하는 리스트를 생성합니다.
    for idx, value in enumerate(lst[:-1]):
        start_cnt = 0
        end_cnt = 0
        temp = idx
        if value == '(':
            while end_cnt <= start_cnt:
                if lst[temp + 1] == ')':
                    end_cnt += 1
                    temp += 1
                else:
                    start_cnt += 1
                    temp += 1
            if not start_cnt + end_cnt == 1:
                sticks.append((idx, idx + start_cnt + end_cnt))

    print(sticks)

    result = 0

    for i, j in sticks:
        for k in lasers:
            if i < k < j:
                result += 1

    print('#{} {}'.format(tc, result + len(sticks)))






# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     lst = ['0'] + list(input()) + ['0']
#     lasers = []
#     length = len(lst)
#     for i in range(len(lst) - 1):
#         if lst[i] + lst[i + 1] == '()':
#             lasers.append(i)
#     cnt = 0
#     for j in lasers:
#         for i in range(1, min(j, length - j + 1)):

# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     lst = ['0'] + list(input()) + ['0']
#     lasers = []
#     for i in range(len(lst) - 1):
#         if lst[i] + lst[i + 1] == '()':
#             lasers.append(i)
#     cnt = 0
#     for j in lasers:
#         temp = j + 2
#         while True:
#             if lst[temp] == '(':
#                 if lst[temp + 1] == ')':
#                     temp += 2
#                 else:
#                     temp += 1
#             elif lst[temp] == '0':
#                 break
#
#             else:
#                 cnt += 1
#                 temp += 1
#
#     print(cnt)