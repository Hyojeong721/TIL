import sys
sys.stdin = open('input.txt')


T = int(input())
word_order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(T):
    tc, N = map(int, input()[1:].split())
    words = input().split()

    # word_count: 단어를 key, 단어의 개수를 value로 가지는 딕셔너리
    word_count = {}

    for word in words:
        # cnt: 현재 탐색 위치까지의 word의 개수
        cnt = word_count.get(word, 0) + 1
        word_count[word] = cnt

    print("#{}".format(tc))

    for word in word_order:
        temp = (word + " ") * word_count[word]
        print(temp, end="")
    print()
