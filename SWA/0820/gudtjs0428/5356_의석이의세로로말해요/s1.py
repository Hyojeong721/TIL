import sys
sys.stdin = open('input.txt')

def read_vertically(strings):
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)

    new_string = ''
    for i in range(max_length):
        for j in range(5):
            try:
                new_string += strings[j][i]
            except:
                pass

    return new_string
    # matrix = [[0] * max_length for _ in range(5)]
    # for row in range(5):
    #     for column in range(max_length):
    #         if ma

T = int(input())
for test_case in range(1, T + 1):
    strings = [input() for _ in range(5)]
    print('#{} {}'.format(test_case, read_vertically(strings)))