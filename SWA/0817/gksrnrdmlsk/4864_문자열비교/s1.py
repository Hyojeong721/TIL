import sys
sys.stdin = open('input.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    A = input()
    B = input()

    if A in B:
        print('#%s 1' % tc)

    else:
        print('#%s 0' % tc)