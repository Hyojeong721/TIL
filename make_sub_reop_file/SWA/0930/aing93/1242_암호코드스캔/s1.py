import sys

sys.stdin = open('input.txt')

hex_to_bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

pattern = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


def find():
    ans = 0
    for i in range(N):  # 행
        j = M * 4 - 1  # 열
        while j > 0:  # j값을 아래 코드에서 변화시키기 위해 for 문이 아니라 while 사용
            # 원소의 값이 1이고, 바로 뒤의 값이 0인 경우
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                pwd = []
                for k in range(8):  # 암호코드의 수
                    x = y = z = 0
                    while arr[i][j] == 1:
                        z += 1  # 1의 갯수
                        j -= 1  # 앞으로 앞으로,..
                    while arr[i][j] == 0:
                        y += 1  # 0의 갯수
                        j -= 1  # 앞으로 앞으로,..
                    while arr[i][j] == 1:
                        x += 1  # 1의 갯수
                        j -= 1  # 앞으로 앞으로,..
                    while arr[i][j] == 0:
                        j -= 1  # 앞으로 앞으로,..

                    # 비교해서 암호 찾기
                    MIN = min(x, y, z)
                    pwd.append(pattern[(x//MIN, y//MIN, z//MIN)])

                odd = pwd[7] + pwd[5] + pwd[3] + pwd[1]
                even = pwd[6] + pwd[4] + pwd[2] + pwd[0]

                # 검증
                if (odd * 3 + even) % 10 == 0:
                    ans += odd + even
                # 같은 행에 암호코드 블럭이 겹쳐 있다면 다음 암호 블럭에 도착
                # j를 오른쪽으로 한칸 이동해야함.

                j += 1

            j -= 1
    return ans



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 16진수 -> 2진수 변환해서 입력받기
    arr = [[] for _ in range(N)]
    for i in range(N):
        tmp = input()  # 16진수
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]   # append임

    # for i in arr:
    #     print(*i)
    # 뒤에서 1을 찾아서 그 좌표를 구해야 한다.
    # print('#{} {}'.format(tc, find()))
for i in range(4):
    print(*i)
