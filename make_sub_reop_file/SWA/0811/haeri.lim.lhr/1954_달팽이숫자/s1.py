import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    result = []
    delta =[
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0]
    ]

    arr =[10]

