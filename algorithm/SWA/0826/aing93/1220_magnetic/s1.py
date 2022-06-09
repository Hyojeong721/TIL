import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        state = 0
        for j in range(N):
            if data[j][i] == 1 and state == 0:
                state = 1
            elif data[j][i] == 2 and state == 1:
                count += 1
                state = 0
    print('#{} {}'.format(tc, count))

    # 1은 N의 성질, 2는 S의 성질
    # 테이블 위에 존재하는 이동 가능한 모든 요소의 수를 카운팅 (1 혹은 2)
    # 이동 가능한 존재가 없을 때까지 반복
    # -1, 1
    # 1은 아래로, 2는 위로

    # 전수 조사 시작
    # 모든 요소들을 검사하는 중에
    # 1을 만났다.
        #N극 자성체 -> 아래로만 이동
            # 1. 벽 체크 -> 벽을 벗어나면 사라짐 -> 현재 위치 값 0으로 바뀜
                # 1-1. 사라짐 -> 움직일 수 있는 개체수 -1
            # 2. S극 체크 -> S극과 N극이 만나면 교착상태 -> 3 으로 ( 교착 개수 +1)
                # 2-1. 나와 내 아래가 모두 움직일 수 없게됨 -> 개체수 -2
            # 3. 이미 교착상태 -> 나만 3으로 변경해서 교착상태로 만들어둠 (교착 개수 유지)
                # 3-1. 나만 교착상태 -> 움직 일 수 있는 개체수 -1
            # 움직일 수 있는 개체수 유지
            # 4. N극 만남 -> 대기
            # 5. 아무것도 아니면 -> 한칸 아래로 이동
    # 2를 만났다.
        # 위로만 이동