import sys
sys.stdin = open('input.txt')
# 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면,
# 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램

def search():
    global result

    for i in range(M):
        max_n = n_list[0]

        for j in range(len(n_list)):
            # 화물중에 트럭적재용량에 가장 근접한 화물 찾기
            if n_list[j] <= m_list[i]:
                # max_n 값이 10이고 트럭용량이 5이고 n_list[j]가 5인 경우
                if max_n <= m_list[i]:
                    if max_n < n_list[j]:
                        max_n = n_list[j]
                else:
                    max_n = n_list[j]
        # 골라진 최대화물이 트럭적재용량보다 작으면 적재확정
        if max_n <= m_list[i]:
            result.append(max_n)
            n_list.remove(max_n)
    return

T = int(input())

for tc in range(1, T+1):
    # N = 컨테이너 수 / M = 트럭 수
    N, M = map(int, input().split())
    # N 개의 화물 무게 리스트
    n_list = list(map(int, input().split()))
    # M 개 트럭의 적재 용량
    m_list = list(map(int, input().split()))

    result = []

    search()


    print("#{} {}".format(tc, sum(result)))