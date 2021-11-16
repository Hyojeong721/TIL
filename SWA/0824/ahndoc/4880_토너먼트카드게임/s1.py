import sys
sys.stdin = open('input.txt')

# def check(a, b):
#     if S[a] == 1 and S[b] == 3:   # 가위, 보
#         return a
#     if S[a] == 3 and S[b] == 1:   # 보, 가위
#         return b
#     if S[a] >= S[b]:    # 숫자가 같거나 큰 경우
#         return a
#     else:
#         return b
#
# def divide(start, end):
#
#     if end - start == 0:
#         return end
#
#     elif end - start == 1:
#         return check(start, end)
#
#     return check(divide(start, (start + end) // 2), divide((start+end) // 2 + 1, end))
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     S = list(map(int, input().split()))
#
#
#     print('#{} {}'.format(tc, divide(0, N - 1) + 1))




def divide(i, j):
    if len(cards[i:j+1]) == 2:

        return find([i, j])

    elif len(cards[i:j+1]) == 1:

        return find([i])
    else:
        n = (i + j) // 2
        # if len(cards[n+1:]) == 2:
        #     return find([n+1, n+2])
        # elif len(cards[:n+1]) == 2:
        #     return find([n-1, n])
        # if len(cards[i:n+1]) == 1 or len(cards[n+1:j]) == 1:
        #     return find([n+1])

            # if n == 1:
            #     return cards[0]
            # else:
            #     if cards[0]

        return find([divide(i, n), divide(n+1, j)])





def find(idxes):
    n = len(idxes)
    if n == 1:
        return idxes[0]
    elif n == 2:
        c1 = cards[idxes[0]]
        c2 = cards[idxes[1]]

        if c1 == 1 and c2 == 2:
            return idxes[1]
        elif c1 == 1 and c2 == 3:
            return idxes[0]
        elif c1 == 2 and c2 == 1:
            return idxes[0]
        elif c1 == 2 and c2 == 3:
            return idxes[1]
        elif c1 == 3 and c2 == 1:
            return idxes[1]
        elif c1 == 3 and c2 == 2:
            return idxes[0]
        elif c1 == c2:
            return idxes[0]





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # print(cards)
    # 0 ~ N-1
    # i, (N-1)//2
    # (N-1)//2 + 1, N-1
    ans = divide(0, N-1) + 1
    print('#{} {}'.format(tc, ans))

