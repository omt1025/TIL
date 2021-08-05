L, U = map(int, input().split())
ans = 0

for num in range(L, U+1):
    S = str(num)
    for s in S:
        ans += int(s)
print(ans)