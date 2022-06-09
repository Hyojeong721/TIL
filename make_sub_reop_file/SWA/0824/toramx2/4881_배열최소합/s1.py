import sys
sys.stdin = open('input.txt')

def permutations(head, tail=''):
    global permute
    if len(head) == 0:
        permute.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []
    permute = []
    row = ''
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        row += str(i)
    permutations(row)

    print(permute)

    counts = []
    for x in range(len(permute)):
        count = 0
        for y in range(N):
                count += arr[y][int(permute[x][y])]
        counts.append(count)
    print(counts)
    # result = min(counts)
    #
    # print('#{} {}'.format(test_case, result))