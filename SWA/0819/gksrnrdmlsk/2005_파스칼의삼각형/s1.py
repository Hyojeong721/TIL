import sys
sys.stdin = open('input.txt')

T = int(input())

# 처음부터 삼각형의 전체리스트를 구해놓습니다.
tri = [[1] for _ in range(10)]
tri[1].append(1)
for i in range(2, 10):
    for j in range(i - 1):
        tri[i].append(tri[i-1][j] + tri[i-1][j + 1])
    tri[i].append(1)

for tc in range(1, T+1): # 구해놓은 삼각형에서 순서대로 출력합니다.
    N = int(input())
    print('#{}'.format(tc))
    for k in range(N):
        print(' '.join(map(str, tri[k])))
