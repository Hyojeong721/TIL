import sys
sys.stdin = open('input.txt')

T = int(input())

# B가 총 몇번 했는지 개수 확인
def find_str(A, B):
    i = 0
    typing = 0
    while i <= len(A)-len(B):
        count = 0
        if A[i] == B[0]:
            for j in range(len(B)):
                if A[i+j] == B[j]:
                    count += 1
                    if count == len(B):
                        typing += 1
                        i += count
                else:
                    i += j
                    break
        else:
            i += 1

    return typing

# typing개수를 이용해서 총 타이핑수 확인
def typing_count(A, B, typing):
    result = typing + len(A) - len(B)*typing

    return result


for test_case in range(1,T+1):
    A, B = input().split()
    print('#%d %s' %(test_case, typing_count(A, B, find_str(A, B))))