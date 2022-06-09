def check(idx):
    global total, ans, checked, mat

    if ans > total:
        return

    if idx == N:
        if ans < total:
            total = ans
            return
    for i in range(N):
        if checked[i] == 0:
            checked[i] = 1
            ans += mat[idx][i]
            check(idx+1)
            checked[i] = 0
            ans -= mat[idx][i]

    return total