'''
    58,608 kb / 152 ms / 1,238 lines
'''
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    memory2 = list(input())
    memory3 = list(input())
    len2 = len(memory2)
    len3 = len(memory3)
    change2 = []

    # 원래 숫자 10진수로
    num2 = 0
    num3 = 0
    for i in range(len2-1, -1, -1):
        num2 += int(memory2[i]) * (2 ** (len2-1-i))
    for i in range(len3-1, -1, -1):
        num3 += int(memory3[i]) * (3 ** (len3-1-i))

    # 2진수 바뀔 수 있는 후보들 저장
    for i in range(len2-1, -1, -1):
        if memory2[i] == '0':
            change2.append(num2 + 2 ** (len2-1-i))
        else:
            change2.append(num2 - 2 ** (len2-1-i))

    # 3진수 하나씩 바꾸면서 2진수와 겹치는지 확인
    for j in range(len3-1, -1, -1):
        if memory3[j] == '0':
            temp1 = num3 + 1 * 3 ** (len3-1-j)
            temp2 = num3 + 2 * 3 ** (len3-1-j)
        elif memory3[j] == '1':
            temp1 = num3 + 1 * 3 ** (len3-1-j)
            temp2 = num3 - 1 * 3 ** (len3-1-j)
        else:
            temp1 = num3 - 1 * 3 ** (len3-1-j)
            temp2 = num3 - 2 * 3 ** (len3-1-j)

        if temp1 in change2:
            ans = temp1
            break
        elif temp2 in change2:
            ans = temp2
            break

    print('#{} {}'.format(tc, ans))
