import sys
sys.stdin = open('input.txt')

T = int(input())

# idea
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# now[i] = prev[i-1] + prev[i]


for t in range(1, T+1):
    N = int(input())
    line_prv = [1]
    line_now = []

    print('#{}'.format(t))

    # 파스칼 삼각형의 크기만큼 반복
    for n in range(N):

        # 윗줄의 길이만큼 반복
        for i in range(1, len(line_prv)):
            item = line_prv[i-1] + line_prv[i]
            line_now.append(item)
        line_now.append(1)   # 현재 줄 마지막에 1 추가

        # 현재 줄에 있는 요소들 print
        for t in line_now:
            print(t, end = ' ')
        print()

        line_prv = line_now  # 현재 줄을 이전 줄로
        line_now = [1]   # 현재 줄 리셋 후 1 추가