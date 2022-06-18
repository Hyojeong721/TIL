import sys
sys.stdin = open('input.txt')
T = int(input())

def even_sort(list):
    if len(list) == 1:
        return list
    temp_max = list[0]

    for i in list: