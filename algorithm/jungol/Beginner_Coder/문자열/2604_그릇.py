bowls = input()
ans = 0
before = bowls[0]
for i in range(len(bowls)):
    if i == 0:
        ans += 10
    else:
        if before != bowls[i]:
            ans += 10
        else:
            ans += 5
        before = bowls[i]

print(ans)