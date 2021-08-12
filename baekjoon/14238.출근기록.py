S = input().strip()
L = len(S)
dp = [[[[[0] * 3 for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
ans = [0] * 50

def check(a, b, c, p1, p2):
    if a < 0 or b < 0 or c < 0:
        return False
    if a == 0 and b == 0 and c == 0:
        return True
    if dp[a][b][c][p1][p2]:
        return False
    dp[a][b][c][p1][p2] = True
    ans[L-a-b-c] = 'A'
    if check(a-1, b, c, 0, p1):
        return True
    if p1 != 1:
        ans[L-a-b-c] = 'B'
        if check(a, b-1, c, 1, p1):
            return True
    if p1 != 2 and p2 != 2:
        ans[L-a-b-c] = 'C'
        if check(a, b, c-1, 2, p1):
            return True
    return False
a = 0
b = 0
c = 0
for s in S:
    if s == 'A':
        a += 1
    elif s == 'B':
        b += 1
    elif s == 'C':
        c += 1
if check(a, b, c, 0, 0):
    print(''.join(ans[:L]))
else:
    print(-1)

# for p in per:
#     check = True
#     for i in range(L-1):
#         if p[i] == 'B' and p[i+1] == 'B':
#             check = False
#             break
#         if i + 1 < L and i + 2 < L:
#             if p[i] == 'C' and p[i+1] == 'C' and p[i+2] == 'C':
#                 check = False
#                 break
#     if check:
#         for pp in p:
#             ans += pp
#         break
# if ans == '':
#     print(-1)
# else:
#     print(ans)