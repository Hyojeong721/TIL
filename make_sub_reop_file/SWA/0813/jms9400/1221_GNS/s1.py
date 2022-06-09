import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    TC, M = input().split()
    words = input().split()
    M = int(M)

    my_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }
    reverse_dict = dict(map(reversed, my_dict.items()))
    result = []
    result2 = []

    for word in words:
        result.append(my_dict[word])

    result.sort()

    for r in result:
        result2.append(reverse_dict[r])

    print(TC)
    print(' '.join(result2))

    # 카운팅정렬로도 해결가능 (나열되어있는 리스트에서 각각 인덱스 몇번 등장했는지)











