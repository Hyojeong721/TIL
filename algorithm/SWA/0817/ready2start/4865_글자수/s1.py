import sys
sys.stdin = open("input.txt")


def char_count(x, word):
    """문자열에 포함된 글자의 개수를 구한다.

    Returns:
        문자열(word)에 포함된 글자(x)의 개수 (int)
    """
    count = 0

    for char in word:
        if x == char:
            count += 1

    return count


T = int(input())

for tc in range(1, T + 1):
    str1, str2 = input(), input()
    # max_count: str1의 글자 중 str2에 가장 많은 글자의 개수
    max_count = 0

    for char in set(str1):
        temp = char_count(char, str2)
        if temp > max_count:
            max_count = temp

    print("#{} {}".format(tc, max_count))
