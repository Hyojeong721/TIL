# 4869 종이붙이기
# 케이스 별 접근하여 점화식으로 생각하면 쉽다.
# 세로는 20으로 같기에 가로를 기준으로 생각
# 도식화해서 생각해보면, a_n = a_((n-1)) + 2 * a_((n-2))

import sys
sys.stdin = open("input.txt")

# 테스트 케이스를 받아온다.
T = int(input())
# 함수를 정의한다
def attach_paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return attach_paper(n-1) + 2 * attach_paper(n-2)
for tc in range(1, T+1):
    N = int(input())
    # a_1 a_2 이렇게 점화식 세우고 함수 만들었는데, 가로 길이는 10배수 즉, 10, 20.. 이렇게 진행되기에 10을 나눠서 생각한다.  나눠
    result = attach_paper(N / 10) # 모두 10의 배수 형태이기에 / 사용
    print("#{} {}".format(tc, result))