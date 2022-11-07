from itertools import permutations


def check(k, arr, dun):
    temp = 0
    for idx in arr:
        if k >= dun[idx][0]:
            k -= dun[idx][1]
            temp += 1
        else:
            break
    return temp


def solution(k, dun):
    answer = -1
    size = len(dun)
    ki = [i for i in range(size)]
    arr = list(permutations(ki, size))
    for a in arr:
        answer = max(check(k, a, dun), answer)
    return answer