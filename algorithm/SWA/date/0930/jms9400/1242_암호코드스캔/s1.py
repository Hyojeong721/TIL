import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

password = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 세로 M 가로
    arr = [input() for _ in range(N)]
    lst = []
    answer = []
    temp = []
    dq = deque()

    for i in range(N-1, -1, -1):  # 0만있는 줄은 건너뛰기
        if arr[i] != '0' * M:
            if arr[i] not in temp:
                temp.append(arr[i])

    while temp:
        num = temp.pop(0)
        number2 = ''
        # 16진수를 4자리 2진수로 바꾸기
        for k in num:
            temp2 = format(int(k, 16), '04b')  # 16진수를 4자리 2진수로 만들기
            # temp2 = bin(int(k, 16))
            # if len(temp2[2:]) < 4:
            #     temp2 = '0' * (4-len(temp2[2:])) + temp2[2:]
            # else:
            #     temp2 = temp2[2:]
            number2 += temp2
        number2 = number2.rstrip('0')
        print(number2)






        # if len(number2) % 7 != 0 or number2[0] == '1':
        #     number2 = '0' + number2
        #     while len(number2) % 7 != 0:
        #         number2 = '0' + number2


    #     number = ''
    #     cnt = 0
    #     y = '0'
    #     for x in number2:
    #         if x == y:
    #             cnt += 1
    #         else:
    #             number += str(cnt)
    #             cnt = 1
    #             if y == '0':
    #                 y = '1'
    #             else:
    #                 y = '0'
    #     if cnt != 0:
    #         number += str(cnt)
    #     temp4 = 0
    #     for i in range(0, len(number), 4):
    #         if number[i: i+4] in password:
    #             temp4 = password[number[i: i+4]]
    #         else:
    #             temp4 = password[str(int(number[i: i+4]) // 2)]
    #         answer.append(temp4)
    #     total = 0
    #     for a in range(len(answer)):
    #         if a % 2 == 0:
    #             total += answer[a] * 3
    #         else:
    #             total += answer[a]
    #     if total % 10 == 0:
    #         print('#{} {}'.format(tc, sum(answer)))
    #         break
    #     else:
    #         answer = []
    # if len(answer) == 0:
    #     print('#{} {}'.format(tc, 0))