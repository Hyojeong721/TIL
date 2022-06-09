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

def bs(number, already):
    if already == chance:
        lst.append(''.join(number))
        return

    else: # already >= length - 1인 경우
        for position in range(length - 1):
            maximum = max(number[position:])
            for i in range(position, length):
                if number[position] != maximum and number[i] == maximum:
                    number[position], number[i] = number[i], number[position]
                    bs(number, already + 1)
                    number[position], number[i] = number[i], number[position]

        if is_double(number):
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


        # if is_double(number):
        #     lst.append(''.join(number))
        #     return
        # else:
        #     number[length - 2], number[length - 1] = number[length - 1], number[length - 2]
        #     bs(number, already + 1)
        #     number[length - 2], number[length - 1] = number[length - 1], number[length - 2]

T = int(input())
for tc in range(1, T + 1):
    number, chance = input().split()
    number = list(number)
    chance = int(chance)
    length = len(number)
    lst = []
    bs(number, 0)
    print('#{} {}'.format(tc, max(lst)))