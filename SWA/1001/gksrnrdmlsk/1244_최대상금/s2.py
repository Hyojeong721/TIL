# 가장 빠름
import sys
sys.stdin = open('input.txt')

def is_double(number):
    cnt = {}
    for i in number:
        if cnt.get(i, 0):
            return True
        else:
            cnt[i] = cnt.get(i, 0) + 1
    return False

def bs(number, already, position):
    if already == chance:
        lst.append(''.join(number))
        return

    elif already < chance and position < length - 1:
        if number[position] != max(number[position:]):
            for i in range(position + 1, length):
                if number[i] == max(number[position:]):
                    number[i], number[position] = number[position], number[i]
                    bs(number, already + 1, position + 1)
                    number[i], number[position] = number[position], number[i]
        else:
            bs(number, already, position + 1)

    else: # already >= length - 1인 경우
        if state:
            lst.append(''.join(number))
            return
        else:
            if (chance - already) % 2:
                number[length - 2], number[length - 1] = number[length - 1], number[length - 2]
                lst.append(''.join(number))
                number[length - 2], number[length - 1] = number[length - 1], number[length - 2]
                return
            else:
                lst.append(''.join(number))
                return

T = int(input())
for tc in range(1, T + 1):
    number, chance = input().split()
    number = list(number)
    chance = int(chance)
    length = len(number)
    state = 1 if is_double(number) else 0
    lst = []
    bs(number, 0, 0)
    print('#{} {}'.format(tc, max(lst)))
