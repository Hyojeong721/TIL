import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 간선개수 E, 루트노드 N
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_set = []

    for e in range(E):
        arr_set.append(list([arr[e*2],arr[e*2+1]]))

    ans = []
    ans.append(N)
    cnt = 0

    while ans != []:
        q = ans.pop(-1)
        cnt += 1

        for i in range(E):
            if q == arr_set[i][0]:
                ans.append(arr_set[i][1])

    print("#{} {}".format(tc, cnt))


