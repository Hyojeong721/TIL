import sys
sys.stdin = open('input.txt')


passwords = ['3211', '2221', '2122', '1411', '1132',
             '1231', '1114', '1312', '1213', '3112']

def find_cypher(lst):
    cnt = 0
    compare = '1'
    cypher = []
    pw = ''
    stretch = 0

    bound = 0
    for bit in lst[::-1]:
        if bit == compare:
            cnt += 1
        else:
            pw = str(cnt) + pw
            cnt = 1
            compare = bit

        if len(pw) == 4:
            # 가로 길이가 넓어진 비율(stretch) 맨 처음 검사
            if not stretch:
                temp = 0
                for i in pw:
                    temp += int(i)
                stretch = temp // 7

            # 넓어진 비율만큼 줄임
            if stretch > 1:
                password = ''
                for i in range(4):
                    password += str(int(pw[i])//stretch)
            else:
                password = pw

            # 암호 맨 앞에 숫자 삽입
            if password in passwords:
                cypher.insert(0, passwords.index(password))
                pw = ''
            else:
                return False, 0

            if len(cypher) == 8:
                break

    if len(cypher) == 7 and len(pw) == 3:
        temp = stretch * 7 - sum(int(j) for j in pw)
        pw = str(temp//stretch) + pw
        cypher.insert(0, passwords.index(pw))

    return cypher, stretch


def is_cypher(cypher):
    """
    암호코드가 정상적인지 검사

    Returns:
        (유효한 경우) 암호코드의 합(int)
        (유효하지 않은 경우) 0

    """
    total = 0

    for i in range(8):
        if i % 2:
            total += cypher[i]
        else:
            total += cypher[i] * 3

    if total % 10 == 0:
        return sum(cypher)
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 2진수로 변환한 배열
    arr = []
    for _ in range(N):
        nums = input()
        temp = ''
        for num in nums:
            temp += format(int(num, 16), 'b').zfill(4)
        arr.append(temp)

    # 16진수에서 2진수로 바뀌며 가로 4배 길어짐
    M *= 4

    # 배열 순회
    r, c = 0, M - 1
    while 0 <= r < N and 0 <= c < M:
        # 행에 1이 없으면 다음 행으로 이동
        if '1' not in arr[r]:
            r += 1
            continue

        # 마지막 열부터 감소하며 1을 찾음
        if arr[r][c] == '0':
            c -= 1

        # 1을 찾으면 암호코드인지 검사
        else:
            # 1번째 줄 검사
            cypher, stretched = find_cypher(arr[r][:c+1])

            # 2~5번째 줄 검사
            cnt = 1
            for i in range(1, 5):
                cyp, stt = find_cypher(arr[r+i][:c+1])
                if cyp == cypher and stt == stretched:
                    cnt += 1

            # 암호 코드가 맞다면 정상인지 검사 후, 출력값에 추가
            ans = 0
            if cnt == 5:
                ans += is_cypher(cypher)
                c -= 56 * stretched
                r += 5 * stretched
            else:
                c -= 1

        # 가능한 길이가 암호코드의 길이보다 짧아지면 다음 행으로 이동
        if c < 55:
            r += 1
            c = M - 1

    print('#{} {}'.format(tc, ans))