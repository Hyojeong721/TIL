import sys
sys.stdin = open("input.txt")


T = int(input())
# pascals[i]: 파스칼 삼각형의 i번째 줄의 수들
pascals = [[], [1], [1, 1]]


for tc in range(1, T + 1):
    n = int(input())

    print("#{}".format(tc))
    p_len = len(pascals)

    # pascals 배열에 n번째 줄까지의 값이 없다면
    if n >= p_len:
        # pascals 배열에 저장되지 않은 첫번째 줄부터 n번째 줄까지 저장한다.
        for i in range(p_len, n + 1):
            # i번째 줄의 파스칼의 삼각형의 값은
            # 1로 시작해서 1로 끝나고 그 사이에는 i - 1번째 줄의 인접 값들의 합으로 구성된다.
            temp = [1]
            for j in range(1, i - 1):
                temp.append(pascals[i - 1][j - 1] + pascals[i - 1][j])
            temp.append(1)

            pascals.append(temp)

    for i in range(1, n + 1):
        print(' '.join(map(str, pascals[i])))
