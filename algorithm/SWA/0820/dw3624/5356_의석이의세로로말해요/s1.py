import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    text = [[i for i in input()] for _ in range(5)]
    result = ''

    for col in range(15):
        for row in range(5):
            try: result += text[row][col]
            except: pass

    print('#{} {}'.format(t, result))