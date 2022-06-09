# 실패한 풀이

import sys
sys.stdin = open('input.txt')

def is_double(number):
    cnt = {}
    for i in number:
        if cnt.get(i, 0):
            return True
        else:
            cnt[i] += 1
    return False

def find_maxis(number):
    maximum = max(number)
    result = []
    for i in range(len(number)):
        if number[i] == maximum:
            result.append(i)
    return result

def biggest(number, chance):
    if chance == 0:
        return number
    else:
        if len(number) >= 3 and number[0] != max(number):
            candidates = []
            if len(find_maxis(number)) >= 2:
                for i in find_maxis(number):
                    temp = number[:]
                    temp[0], temp[i] = temp[i], temp[0]
                    candidates.append(''.join(temp))
                for i in range(len(candidates) - 1, -1, -1):
                    if candidates[i] == max(candidates):
                        number[0], number[find_maxis(number)[i]] = number[find_maxis(number)[i]], number[0]
                return [max(number)] + biggest(number[1:], chance - 1)

            else:
                number[0], number[len(number) - number[::-1].index(max(number)) - 1] = max(number), number[0]
                return [max(number)] + biggest(number[1:], chance - 1)





        elif len(number) >= 3:
            return [max(number)] + biggest(number[1:], chance)

        elif len(number) == 2:
            if number[0] >= number[1]:
                if len(find_maxis(N)) >= 2 or chance % 2 == 0:
                    return number
                else:
                    return number[::-1]
            else:
                if len(find_maxis(N)) >= 2:
                    if chance >= 1:
                        return number[::-1]
                else:
                    if chance % 2:
                        return number[::-1]
                    else:
                        return number

        else:
            return number


T = int(input())
for tc in range(1, T + 1):
    number, chance = input().split()
    number = list(number)
    chance = int(chance)
    N = number[:]
    print(biggest(number, chance))
