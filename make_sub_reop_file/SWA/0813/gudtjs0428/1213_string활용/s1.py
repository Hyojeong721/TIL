import sys
sys.stdin = open('input.txt')

def how_many_in_string(find_this, find_from_here):
    count = 0
    for i in range(len(find_from_here)):
        string = find_from_here[i:i+len(find_this)]
        if string == find_this:
            count += 1
    return count


T = 10
for tc in range(1, T + 1):
    input()
    find_this = input()
    find_from_here = input()
    print('#{} {}'.format(tc, how_many_in_string(find_this, find_from_here)))