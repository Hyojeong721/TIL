# 백프로 참고하고 이해함.

# numbers안에 수를 이용해 +, -으로 타켓 수를 만드는 방법의 수
def solution(numbers, target):
    answer = 0
    def dfs(num, i):
        nonlocal answer
        # 모든 수를 합했을때 비교
        if i == len(numbers):
            if num == target:
                answer += 1
            return

        signs = [num, -num]
        if i == 1:
            for k in range(2):
                dfs(signs[k]+numbers[i], i+1)
                dfs(signs[k]-numbers[i], i+1)
        else:
            dfs(num+numbers[i], i+1)
            dfs(num-numbers[i], i+1)

    dfs(numbers[0], 1)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))