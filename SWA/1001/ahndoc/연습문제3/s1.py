numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
C = []
# n개에서 r개를 고르는 조합, s: 선택할 수 있는 구간의 시작, k: 고른 개수
# 10개에서 3개를 고르는 조합 / / / / / / / /x/ / /
"""
0

0 1 2 3 4 5 6 7 8 9   0~7
  1 2 3 4 5 6 7 8 9   1~8
"""
ans = []
def find(n, r, s, k):
    global C
    if k == r:

        if sum(C) == 0 and C not in ans:
            ans.append(C)
            C = []
            return

        C = []
        return
    else:
        for i in range(s, n+1-r+k):
            C.append(numbers[i])

            find(n, r, i+1, k+1)

result = []
for i in range(11):
    find(10, i, 0, 0)
    for j in ans:
        if j and j not in result:
            result.append(j)
            print(j)


