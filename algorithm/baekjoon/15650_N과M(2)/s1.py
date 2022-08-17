import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

def su(temp, res):
    if len(arr) == M:
        print(*arr)
        return

    if len(temp) == M:
        temp_2 = temp[:]
        temp_2.sort()
        if temp_2 not in res:
            res.append(temp_2)
            print(*temp_2)
            return

    for i in arr:
        if i not in temp:
            temp.append(i)
            su(temp, res)
            temp.pop()

su([], [])

