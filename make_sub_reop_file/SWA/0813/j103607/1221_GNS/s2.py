import sys
sys.stdin = open('input.txt')

T = int(input())
word_order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(T):
    tc, N = map(int, input()[1:].split())

    # 단어를 key, 단어의 개수를 value로 가지는 딕셔너리
    word_count = dict()
    words = input().split()

    for word in words:
        cnt = word_count.get(word, 0) + 1
        word_count[word] = cnt

    print("#{}".format(tc))

    for word in word_order:
        for _ in range(word_count[word]):
            print(word, end=" ")
    print()