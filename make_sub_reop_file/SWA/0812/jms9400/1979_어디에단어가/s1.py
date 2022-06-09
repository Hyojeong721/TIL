import sys
import copy
sys.stdin = open('input.txt')

T = int(input())


def find_word1(a, b):
    cnt = 0
    while b < N:
        #우로 탐색
        word_box[a][b] = 0
        cnt += 1
        if b+1 in range(N) and word_box[a][b+1] == 1:
            b += 1
        else:
            break

    if cnt == K:
        return 1
    else:
        return 0

def find_word2(a, b):
    cnt = 0
    while b < N:
        #아래로 탐색
        word_box2[a][b] = 0
        cnt += 1
        if a+1 in range(N) and word_box2[a+1][b] == 1:
            a += 1
        else:
            break

    if cnt == K:
        return 1
    else:
        return 0



for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    word_box = [list(map(int, input().split())) for _ in range(N)]
    # word_box.append([0]*(N+1)) 마지막에 띠를둘러서 계산하기 편하게
    word_box2 = copy.deepcopy(word_box)
    result = 0

    for i in range(N):
        for j in range(N):
            if word_box[i][j] == 1:
                result += find_word1(i, j)
            if word_box2[j][i] == 1:
                result += find_word2(j, i)

    print('#{} {}'.format(tc, result))












# def find_word1(a, b, K):
#     total = 0
#     for n in range(K):
#         total += word_box[a][b + n]
#     if total == K:
#         return 1
#     else:
#         return 0
#
# def find_word2(a, b, K):
#     total = 0
#     for n in range(K):
#         total += word_box[a+n][b]
#     if total == K:
#         return 1
#     else:
#         return 0


    # result = 0
    #
    # # 가로 탐색
    # for i in range(N):
    #     for j in range(N):
    #
    #         if word_box[i][j] == 1 and j + K < N:
    #             if j + K == N - 1:
    #                 result += find_word1(i, j, K)
    #             elif word_box[i][j+K] == 0:
    #                 result += find_word1(i, j, K)
    #
    #         if word_box[j][i] == 1 and j + K < N:
    #             if j + K == N - 1:
    #                 result += find_word2(j, i, K)
    #             elif word_box[j+K][i] == 0:
    #                 result += find_word2(j, i, K)
    # print(result)