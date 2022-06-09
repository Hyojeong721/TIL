import sys
sys.stdin = open('input.txt')

def check_run(arr, x):
    if x-1 in arr and x+1 in arr:
        return True
    elif x+1 in arr and x+2 in arr:
        return True
    elif x-1 in arr and x-2 in arr:
        return True
    else:
        return False

def check_triplet(arr, x):
    if arr.count(x) == 3:
        return True
    else:
        return False

for test_case in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    winner = 0

    for i in range(len(cards)):
        if i % 2 == 0:
            p1.append(cards[i])
            p1.sort()
            if check_run(p1, cards[i]) or check_triplet(p1, cards[i]):
                winner = 1
                break
        else:
            p2.append(cards[i])
            p2.sort()
            if check_run(p2, cards[i]) or check_triplet(p2, cards[i]):
                winner = 2
                break

    print('#{} {}'.format(test_case, winner))

