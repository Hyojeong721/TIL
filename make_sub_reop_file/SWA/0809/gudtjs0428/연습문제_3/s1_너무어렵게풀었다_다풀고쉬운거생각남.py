import sys
sys.stdin = open('input.txt')

# 심지어 원래도 쉬운거 생각했던거 같은데....
# 생각처럼 안되네
# 2차원 배열 만들어서 1로 체크하고 맨 위 인덱스 - 밑에것들 합 중 젤 큰거 반환하면 될거같은데
# 효율성이 너무 떨어지는거 같은데

def gravity(width, blocks):
    max_fall = 0
    tmp = blocks
    blocks_to_minus = []
    for _ in range(width):
        longest = max(blocks)
        fall = width - blocks.index(longest) - blocks.count(longest)
        if fall > max_fall:
            max_fall = fall
        while tmp[tmp.index(max(tmp))] == longest:
            blocks_to_minus.append(tmp.index(max(tmp)))
            tmp[tmp.index(max(tmp))] = 0
        for i in range(len(blocks_to_minus)):
            blocks[blocks_to_minus[i]] = max(tmp)
        if max(tmp) == 0:
            break

    return max_fall


T = int(input())
for test_case in range(1, T + 1):
    width = int(input())
    blocks = list(map(int, input().split()))
    print(gravity(width, blocks))