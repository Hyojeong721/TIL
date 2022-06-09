data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(data)
cnt = [0] * 10

def powerset(idx):
    # 부분집합 다 찾지 못한 경우
    if idx < n:
        # cnt[idx]가 0인 경우
        cnt[idx] = 0
        powerset(idx + 1)

        # cnt[idx]가 1인 경우
        cnt[idx] = 1
        powerset(idx+1)

    # 부분집합 다 찾은 경우: idx = N
    else:
        total = 0
        for i in range(n):
            if cnt[i] == 1:
                total += data[i]

        if total == 10:
            for i in range(n):
                if cnt[i] == 1:
                    print(data[i], end=' ')
            print()

powerset(0)