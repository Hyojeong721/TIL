'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
'''
import sys
sys.stdin = open('input.txt')
case = int(input())
i = 0
p = 0
m_stop = list()

listx = list()


def check_f(x):
    ans = 0
    # 지나는 정류장을 임의로 담아줌
    for m in stop:

        if x < m <= (x + k):
            ans = m  # m이 순차적으로 돌면서 저장저장 최댓값 저장됨
    if ans == 0:
        del m_stop[:]
        return

    else:
        m_stop.append(ans)  # m이 추가된다.

    x = ans
    if x >= (n - k):
        return
    else:
        check_f(x)


for i in range(case):
    p = i
    k, n, m = map(int, input().split())  # 최대 정류장 수, 정류장 수, 충전기가 설치된 정류장의 개수
    stop = list(map(int, input().split()))
    x = 0
    m_stop = []
    check_f(x)

    print(f"#{p + 1} {len(m_stop)}")
