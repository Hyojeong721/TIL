n = int(input())
arr = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def go(row, col, idx, ans):
    num = n * (1+n) // 2
    dr = [1, 0, -1]
    dc = [1, -1, 0]

    while num != 0:
        if ans == 10:
            ans = 0
        # 유효 공간이라면
        if 0 <= row < n and 0 <= col < n:
            # 방문 했던 곳이라면
            if visited[row][col] == 1:
                # 전의 자리로 가서
                row -= dr[idx]
                col -= dc[idx]
                # 새로운 방향 전환
                idx += 1
                idx = idx % 3
                # 새자리로
                row += dr[idx]
                col += dc[idx]

                # 첫 방문이면 값 저장
                if visited[row][col] != 1:
                    arr[row][col] = ans
                    ans += 1
                    visited[row][col] = 1
                    # 다음자리 만들기
                    row += dr[idx]
                    col += dc[idx]

            # 첫방문이라면
            else:
                arr[row][col] = ans
                visited[row][col] = 1
                ans += 1
                row += dr[idx]
                col += dc[idx]

        # 아웃라인이라면
        else:
            # 전의 자리로 돌아가고
            row -= dr[idx]
            col -= dc[idx]
            # 새로운 방향 전환
            idx += 1
            idx = idx % 3
            # 새로운 자리로 가서
            row += dr[idx]
            col += dc[idx]
            # 첫 방문이면 값 저장
            if visited[row][col] != 1:
                arr[row][col] = ans
                ans += 1
                visited[row][col] = 1
                # 다음자리 만들기
                row += dr[idx]
                col += dc[idx]

            else:
                print('break', row, col, idx, ans)
                break

        num -= 1



go(0, 0, 0, 0)

for i in range(n):
    res = arr[i][:i+1]
    print(*res)