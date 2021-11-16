import sys
sys.stdin = open('input.txt')

TC = int(input())

for test_case in range(TC):
    str1 = input()      # abccc
    str2 = input()      # dsfaggdvasbdc
    set1 = set(str1)    # {'c', 'b', 'a'}
    strboard = ''       # dbaabcc

    for i in range(len(str2)):
        if str2[i] in set1:
            strboard += str2[i]

    board = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
        "G" : 0,
        "H" : 0,
        "I" : 0,
        "J" : 0,
        "K" : 0,
        "L" : 0,
        "M" : 0,
        "N" : 0,
        "O" : 0,
        "P" : 0,
        "Q" : 0,
        "R" : 0,
        "S" : 0,
        "T" : 0,
        "U" : 0,
        "V" : 0,
        "W" : 0,
        "X" : 0,
        "Y" : 0,
        "Z" : 0,
    }

    for char in strboard:
        board[char] += 1

    result_board = list(board.values())

    print("#{} {}".format(test_case + 1, max(result_board)))