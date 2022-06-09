import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):

    case_number = int(input())

    target = input()
    sentence = input()

    # for문 돌면서 target 글자수와 같은 범위 인덱스값 == target이면 count +1
    count = 0
    for i in range(len(sentence)):
        if sentence[i:i+len(target)] == target:
            count += 1
    print('#{} {}'.format(tc, count))

    # count함수 활용
    # result = sentence.count(target)
    # print(result)
