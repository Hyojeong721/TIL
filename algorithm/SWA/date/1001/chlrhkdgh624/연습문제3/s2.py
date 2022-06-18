# 부분집합 합 문제 구현하기: 재귀
sample_set = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
subsets = []


def comb(n, r):
    if r == 0:
        if sum(tmp) == 0:
            # print(tmp)
            subsets.append(tmp[:])
            # 그냥 tmp를 append하면 deepcopy가 되지 않아 중복현상이 발생한다!
        return
    else:
        if n < r:
            return
        else:
            tmp[r-1] = sample_set[n-1]
            comb(n-1, r-1)
            comb(n-1, r)


for i in range(11):
    tmp = [0]*i
    comb(10, i)

print(subsets)

