import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    t, E = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print('t:', t, 'E(순서쌍의 개수):', E)

    arr = {}
    for i in range(E):
        start_node = numbers[2*i]       # 짝수 번째 요소는 현재 노드
        next_node = numbers[2*i + 1]    # 홀수 번째 요소는 다음 노드
        arr[start_node] = arr.get(start_node, []) + [next_node]
            # get(key, default) + [item]
            ## key 값에 해당하는 value 값 반환(없는 경우 기본값 반환)
            ## value값 list에 [item]을 추가   ex) [0] + [1] ==> [0, 1]

        # print('idx:', i, ' 현재 노드: ', start_node, ' 다음 노드:', next_node)

    # print('arr:', arr)   # 딕셔너리 형태로 저장된 경로 그래프 확인

    stack = [0]     # 시작점 0
    visit = [0] * 100   # visit 여부 확인용 list

    while stack:    # stack에 값이 있는 경우 반복
        v = stack.pop()     # stack의 마지막 값(마지막 방문 노드)
        visit[v] = 1        # 마지막 방문 노드의 방문 여부 갱신

        if v in arr.keys():     # 딕셔너리 key에 v(마지막 방문 노드)가 있는 경우
            for w in arr[v]:    # 해당 노드에서 연결되는 다음 노드 탐색
                if visit[w] == 0:   # 다음 노드에 방문하지 않은 경우
                    stack.append(w)     # stack에 해당 노드 추가, 반복
        # print('stack:', stack)

    result = visit[-1]  # 목표 노드에 도착했다면 1 반환
    print('#{} {}'.format(t, result))