import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
bulb = list(map(int, input().split()))
l = len(switch)
idx = [0] * l

for i in range(l):
    for j in range(l):
        if switch[i] == bulb[j]:
            idx[j] = i
            break
print(idx)
dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if idx[i] > idx[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if idx[i] < idx[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
print(dp1, dp2)
ans = []
mx1, mx2 = max(dp1), max(dp2)
if mx1 >= mx2:
    mx_id = dp1.index(mx1)
    while mx_id >= 0:
        if dp1[mx_id] == mx1:
            ans.append(bulb[mx_id])
            mx1 -= 1
        mx_id -= 1
else:
    mx_id = dp2.index(mx2)
    while mx_id >= 0:
        if dp2[mx_id] == mx2:
            ans.append(bulb[mx_id])
            mx2 -= 1
        mx_id -= 1
ans.sort()
print(len(ans))
print(*ans)
'''
2 4 1 5 3
4 5 1 3 2
1 3 2 4 0
'''