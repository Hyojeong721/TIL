import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = []
    result = []
    for n in range(N): # 각 문자로 이루어진 리스트를 만듭니다.  #[['a', 'b'], ...] 이런 식으로
        elems = []
        elems.extend(input())
        lst.append(elems)

    for r in range(N): # 행별로 탐색합니다.
        for c in range(N - M + 1):
            if lst[r][c:c + M] == lst[r][c:c + M][::-1]:
                result = lst[r][c:c + M]

    for c in range(N): # 열별로 탐색합니다.
        for r in range(N - M + 1):
            if [lst[r + i][c] for i in range(M)] == [lst[r + i][c] for i in range(M)][::-1]:
                result = [lst[r + i][c] for i in range(M)]

    print('#{} {}'.format(tc, ''.join(result)))