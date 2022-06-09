import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    # 파리채로 잡은 파리 숫자합의 리스트
    total_list = []
    # 파리채의 시작점 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리채로 잡은 파리 숫자
            total = 0
            # 파리채 면적 내 파리 숫자 합 구하기
            for x in range(M):
                for y in range(M):
                    total += matrix[i+x][j+y]
            total_list.append(total)

        max_value = total_list[0]
        for j in range(1, len(total_list)):
            if max_value < total_list[j]:
                max_value = total_list[j]
    print('#{0} {1}'.format(test_case, max_value))


