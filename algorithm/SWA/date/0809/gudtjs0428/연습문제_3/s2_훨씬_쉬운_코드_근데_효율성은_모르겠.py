import sys
sys.stdin = open('input.txt')

def gravity(width, blocks):
    max_fall = 0
    fall = 0
    for i in range(len(blocks)):
        for j in range(i+1, len(blocks)):
            if blocks[i] > blocks[j]:
                fall += 1
        if fall > max_fall:
            max_fall = fall
        fall = 0
        if max_fall >= width - (i+1):
            return max_fall

    # max_fall = 0
    # for i in range(len(blocks) - 1):
    #     if blocks[i] == max(blocks):
    #         fall = width - i - blocks.count(blocks[i])
    #         if fall > max_fall:
    #             max_fall = fall
    #         blocks[i] = 0
    #
    # return max_fall


T = int(input())
for test_case in range(1, T + 1):
    width = int(input())
    blocks = list(map(int, input().split()))
    print(gravity(width, blocks))