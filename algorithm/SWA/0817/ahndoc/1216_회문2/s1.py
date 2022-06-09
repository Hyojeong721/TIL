import sys
sys.stdin = open('input.txt')

# # 회문 체크 함수
# def check(s):
#     st = 0
#     ed = len(s) - 1
#     while st < ed and s[st] == s[ed]:
#         st += 1
#         ed -= 1
#     if st >= ed:
#         return True
#     return False
# # 가장 긴 회문의 길이를 찾는 함수
# def arrcheck(M):
#     for i in range(N):
#         for st in range(N-M+1):
#             result = check(ARR[i][st:st+M])
#             if result:
#                 return ARR[i][st:st+M]
#
#             tmp_str = ''
#             for k in range(st, st+M):
#                 tmp_str += ARR[k][i]
#             result = check(tmp_str)
#             if result:
#                 return tmp_str

# def check(words):
#     i = -1
#     while i < len(words) // 2:
#         i += 1
#         if words[i] != words[-1 - i]:
#             return False
#     return True

T = 10
for tc in range(1, T + 1):
    NO = int(input())
    N = 100
    # ARR = [input() for _ in range(N)]
    #
    # for M in range(N-1, 1, -1):
    #     result = arrcheck(M)
    #     if result:
    #         print('#{} {}'.format(tc, len(result)))
    #         break


############################################################################


    board = [input() for _ in range(N)]

    row_v = 0
    cnt = 0
    for k in range(N, 0, -1):
        if cnt == 2:
            break
        for j in range(N-k+1):
            if cnt == 1:
                cnt += 1
                break
            for i in range(N):
                if board[i][j:j+k] == board[i][j:j+k][::-1]:
                    cnt += 1
                    row_v = k
                    break
    col_list = []
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += board[j][i]
        col_list.append(temp)

    col_v = 0
    cnt = 0
    for k in range(N, 0, -1):
        if cnt == 2:
            break
        for j in range(N-k+1):
            if cnt == 1:
                cnt += 1
                break
            for i in range(N):
                if col_list[i][j:j+k] == col_list[i][j:j+k][::-1]:
                    cnt += 1
                    col_v = k
                    break
    if row_v > col_v:
        print('#{} {}'.format(tc, row_v))
    else:
        print('#{} {}'.format(tc, col_v))



