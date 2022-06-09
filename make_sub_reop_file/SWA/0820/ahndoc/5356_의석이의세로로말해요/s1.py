import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    max_len = len(words[0])
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    print('#{}'.format(tc), end=' ')
    for i in range(max_len):
        for j in range(5):
            if len(words[j]) > i:
                print(words[j][i], end='')
    print()




  # # 1.
  #   word = [0] * 5
  #
  #   # 가장 긴 word의 length 도출
  #   max_len = 0
  #   for i in range(5):
  #       word[i] = list(input())
  #       if len(word[i]) > max_len:
  #           max_len = len(word[i])
  #
  #   print('#{} '.format(tc), end='')
  #   for i in range(max_len):
  #       for j in range(5):
  #           # 1. 허락받고 쓰자
  #           if len(word[j]) > i:
  #               print(word[j][i], end='')
  #   print()

    # 2. 허락 대신 용서를 구하자
    #             try:
    #                 print(word[j][i], end='')
    #             except:
    #                 pass
    # print()