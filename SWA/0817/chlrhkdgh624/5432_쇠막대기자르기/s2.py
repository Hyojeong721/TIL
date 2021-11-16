import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arrange = input()
    idxs = []
    bars = ''
    count = 0

    for idx, x in enumerate(arrange):
        bars += x
        idxs.append(idx)
        if bars[-2:] == '()':
            bars = bars[:-2]
            j = idxs.pop(-1)
            i = idxs.pop(-1)
            if len(arrange[i:j+1]) == 2:
                pass
            else:
                count += arrange[i:j+1].count('()') + 1

    print(f'#{tc} {count}')
