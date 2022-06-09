import sys
sys.stdin = open('input.txt')
T = 10

for tc in range(1,T+1):
    case = input()
    #str type으로 input
    target = input()
    arr = input()

    #문자열 길이
    K = len(target)
    N = len(arr)
    total = 0
    for i in range(N):
        pb = arr[i]
        for j in range(K):
            if arr[i] == target[j] and i + K <= N:
                for k in range(K):
                    if arr[i + k] != target[k]:
                        break
                    elif k == K - 1:
                        total += 1



    print('#{} {}'.format(tc, total))

