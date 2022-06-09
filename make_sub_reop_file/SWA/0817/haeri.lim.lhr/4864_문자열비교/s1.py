import sys
sys.stdin = open('input.txt')

T = int(input())

def find_str(N, M):
    i = 0
    while i <= len(M)-len(N) + 1:
        count = 0

        if M[i] == N[0]:
            for j in range(len(N)):
                if M[i+j] == N[j]:
                    count += 1
                    if count == len(N):
                        return 1
                else:
                    i = i+j
                    break

        i += 1

    return 0


for test_case in range(1,T+1):
    N = input()
    M = input()
    print('#%d %s' %(test_case, find_str(N, M)))