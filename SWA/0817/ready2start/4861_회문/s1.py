import sys
sys.stdin = open("input.txt")


def get_palindrome(words, N, pld_length):
    """단어 리스트 words에서 가로 or 세로에 존재하는 회문을 구한다.

    Args:
        N: 단어의 개수, 단어 하나의 길이 (int)
        pld_length: 찾아야 하는 회문의 길이 (int)
    Returns:
        words 내에 존재하는 회문 (str)
    """

    # 1. 가로 회문 탐색
    for r in range(N):
        for c in range(N - pld_length + 1):
            # start_idx, end_idx: 탐색 중인 문자열의 시작 인덱스, 끝 인덱스
            # 양 끝에서부터 한 칸씩 안으로 들어가며 같은 문자인지 검사한다.
            start_idx, end_idx = c, c + pld_length - 1
            for i in range(pld_length // 2 - 1):
                # 양쪽에서 비교하여 같은 문자가 아니면 탐색을 중단한다.
                if words[r][start_idx] != words[r][end_idx]:
                    break
                start_idx += 1
                end_idx -= 1
            else:
                return words[r][c:c + pld_length]

    # 2. 세로 회문 탐색
    for c in range(N):
        for r in range(N - pld_length + 1):
            start_idx, end_idx = r, r + pld_length - 1
            for i in range(pld_length // 2 - 1):
                if words[start_idx][c] != words[end_idx][c]:
                    break
                start_idx += 1
                end_idx -= 1
            else:
                temp = ''
                for cnt_r in range(r, r + pld_length):
                    temp += words[cnt_r][c]
                return temp


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    words = []

    for _ in range(N):
        words.append(input())

    pld = get_palindrome(words, N, M)

    print("#{} {}".format(tc, pld))
