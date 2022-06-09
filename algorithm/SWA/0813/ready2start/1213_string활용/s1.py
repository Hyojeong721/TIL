import sys
sys.stdin = open("input.txt", encoding="UTF-8")


def count_string(target, sentence):
    """
    문장 내의 특정 문자열의 개수를 구한다.

    target: 찾을 문자열
    sentence: 문자열을 검색할 문장
    count: <sentence> 내의 <target>의 개수
    """
    count = 0
    T, S = len(target), len(sentence)

    for i in range(S - T + 1):
        j = 0
        while j < T:
            if target[j] != sentence[i + j]:
                break
            j += 1

        if j == T:
            count += 1

    return count


T = 10

for _ in range(T):
    tc = int(input())
    target = input().rstrip()
    sentence = input().rstrip()

    word_count = count_string(target, sentence)
    print("#{} {}".format(tc, word_count))
