def perm(n, k):
    global status

    if k == n:
        if p[:3] == [p[0]] * 3:
            if p[3:] == [p[3]] * 3:
                status = 1
            elif p[3:] == [p[3]] + [p[3] + 1] + [p[3] + 2]:
                status = 1
        elif p[:3] == [p[0]] + [p[0] + 1] + [p[0] + 2]:
            if p[3:] == [p[3]] * 3:
                status = 1
            elif p[3:] == [p[3]] + [p[3] + 1] + [p[3] + 2]:
                status = 1
    else:
        for i in range(n):
            if used[i] == 0:
                used[i] = 1
                p[k] = arr[i]
                perm(n, k+1)
                used[i] = 0

p = [0] * 6
# arr = [1, 2, 4, 7, 8, 3]
# arr = [6, 6, 7, 7, 6, 7]
# arr = [0, 5, 4, 0, 6, 0]
arr = [1, 0, 1, 1, 2, 3]
used = [0] * 6
status = 0
perm(6, 0)
temp = 0

if status == 1:
    print('baby-gin')
else:
    print('not baby-gin')
