tri = ['111', '222', '333', '444', '555', '666', '777', '888', '999']
run = ['123', '234', '345', '456', '567', '678', '789']
answer = 'LOSE!'
def perm(cards, n, k):
    global answer
    if k == n:
        result = []
        for j in range(n):
            result.append(cards[p[j]])

        result = ''.join(list(map(str, result)))
        ans = 0
        if result[:3] in tri:
            ans += 1
        if result[3:] in tri:
            ans += 1
        if result[:3] in run:
            ans += 1
        if result[3:] in run:
            ans += 1

        if ans >= 2:
            answer = 'baby-gin!'
        return

    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                p[k] = arr[i]
                perm(cards, n, k + 1)
                used[i] = 0




arr = [0, 1, 2, 3, 4, 5]
used = [0] * 6
p = [0] * 6

C = [2, 3, 4, 7, 7, 7]
perm(C, 6, 0)
print(answer)