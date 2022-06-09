


def solution(n):
    answer = 0
    N = n
    arr = [[0] * n for _ in range(n)]
    cnt = 1
    col = -1
    row = 0
    trans = 1
    # 달팽이
    while n > 0:
        for i in range(n):
            col += trans
            arr[row][col] = cnt
            cnt += 1
        n -= 1
        for j in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1
    for k in range(N):
        answer += arr[k][k]
    return answer

n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")