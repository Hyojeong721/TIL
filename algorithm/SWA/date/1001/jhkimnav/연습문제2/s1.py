'''
4
124783
667767
054060
101123
'''

def P(chosen, used, n):
    global baby_gin
    if len(chosen) == n:
        cnt = 0
        # print(chosen)
        # RUN
        if chosen[0] + 1 == chosen[1] and chosen[1] + 1 == chosen[2]:
            cnt += 1
        if chosen[3] + 1 == chosen[4] and chosen[4] + 1 == chosen[5]:
            cnt += 1

        # Triplet
        if chosen[0] == chosen[1] and chosen[1] == chosen[2]:
            cnt += 1
        if chosen[3] == chosen[4] and chosen[4] == chosen[5]:
            cnt += 1
        if not baby_gin and cnt == 2:
            print('#{} baby-gin'.format(tc+1))
            baby_gin = True

        return
    else:
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                P(chosen, used, 6)
                used[i] = 0
                chosen.pop()


T = int(input())
for tc in range(T):
    # arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = list(map(int, input()))
    used = [0] * len(arr)
    baby_gin = False
    P([], used, 6)

