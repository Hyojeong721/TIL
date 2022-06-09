import sys
sys.stdin = open('sample_input.txt')
T = int(input())


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))  # N: 화덕 크기, M: 피자 개수
    cheese = list(map(int, input().split()))
    idx_list = [0] * M

    for i in range(M):
        idx_list[i] += i + 1

    baking_list = cheese[:N]
    baking_idx_list = idx_list[:N]
    k = N-1

    test_list = []

    while len(test_list) < M:
        if baking_list[0] != 0:
            a = baking_list.pop(0) // 2
            baking_list.append(a)
            baking_idx_list.append(baking_idx_list.pop(0))
        elif baking_list[0] == 0:
            k += 1
            if k < M:
                baking_list.pop(0)
                baking_list.append(cheese[k])
                test_list.append(baking_idx_list.pop(0))
                baking_idx_list.append(idx_list[k])
            else:
                baking_list.pop(0)
                test_list.append(baking_idx_list.pop(0))

    print(test_list)