import sys
sys.stdin = open('input.txt')

T = int(input())

def palindrome(N,M,input_palindrome):

    if M % 2 == 0:
        result = ''
        for i in range(N):
            count = 0
            j = 0
            while j <= N - M:
                for k in range(M//2):
                    if input_palindrome[i][j+k] == input_palindrome[i][j + M - k - 1]:
                        count += 1
                    else:
                        count = 0
                        j += 1
                    if count == M//2:
                        for k in input_palindrome[i][j: j+M-1]:
                            result += k
                        return result

        for i in range(N):
            count = 0
            j = 0
            while j <= N - M:
                for k in range(M // 2):
                    if input_palindrome[j + k][i] == input_palindrome[j + M - k - 1][i]:
                        count += 1
                    else:
                        count = 0
                        j += 1
                        break
                    if count == M // 2:
                        for k in range(j, j+M-1):
                            result += input_palindrome[k][i]
                        return result
    else:
        result = ''
        for i in range(N):
            count = 0
            j = 0
            while j <= N - M:
                for k in range(M//2):
                    if input_palindrome[i][j+k] == input_palindrome[i][j + M - k - 1]:
                        count += 1
                    else:
                        count = 0
                        j += 1
                        break
                    if count == M//2:
                        for k in input_palindrome[i][j: j+M]:
                            result += k
                        return result
            for i in range(N):
                count = 0
                j = 0
                while j <= N - M:
                    for k in range(M // 2):
                        if input_palindrome[j + k][i] == input_palindrome[j + M - k - 1][i]:
                            count += 1
                        else:
                            count = 0
                            j += 1
                            break
                        if count == M // 2:
                            for k in range(j, j + M):
                                result += input_palindrome[k][i]
                            return result

for test_case in range(1,T+1):
    N, M = list(map(int, input().split()))
    input_palindrome = []
    for i in range(N):
        temp = list(input())
        input_palindrome.append(temp)

    print('#%d %s' % (test_case, palindrome(N,M,input_palindrome)))
