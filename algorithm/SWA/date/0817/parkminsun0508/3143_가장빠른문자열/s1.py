import sys
sys.stdin = open("input.txt")

# 테스트 케이스를 받아온다.
for tc in range(int(input())):
    A, B = input().split()
    C = A.count(B)
    # print(C) 1, 2가 나옴을 알 수 있다.
    #format 자체에 넣어 결과 출력한다.
    print('#{} {}'.format(tc + 1, len(A)-len(B)*C+C))