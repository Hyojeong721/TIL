import sys
sys.stdin = open('sample_input.txt')

T = int(input())


def rotation(num_list, time):
    for _ in range(time):
        rotate = num_list.pop(0)
        num_list.append(rotate)

    return num_list[0]


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = rotation(numbers, M)
    print(f'#{tc} {result}')
