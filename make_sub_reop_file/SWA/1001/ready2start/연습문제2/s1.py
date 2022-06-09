
def get_permutations(arr, k):
    """
    주어진 배열의 숫자들로 만들 수 있는 모든 순열을 구한다. (재귀 함수 이용)
    """
    global permutations, current, visited

    if len(arr) == k:
        permutations.add(current)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            current += arr[i]
            get_permutations(arr, k + 1)
            visited[i] = False
            current = current[:-1]


def check_baby_gin(num):
    """
    주어진 6자리 숫자가 Baby-gin인지 검사한다.
    """
    get_permutations(num, 0)

    for p in permutations:
        check_first = (p[0] == p[1] == p[2]) or (int(p[0]) == int(p[1]) - 1 == int(p[2]) - 2)
        check_second = (p[3] == p[4] == p[5]) or (int(p[3]) == int(p[4]) - 1 == int(p[5]) - 2)

        if check_first and check_second:
            return True

    return False


test_cases = ['124783', '667767', '054060', '101123']

for tc in test_cases:
    permutations = set()
    current = ""
    visited = [False] * len(tc)

    print("{} : {}".format(tc, check_baby_gin(tc)))
