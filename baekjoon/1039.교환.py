from collections import deque
from itertools import combinations

def bfs(N):
    check = set()
    ans = 0
    lencheck = len(q)
    while lencheck:
        x = q.popleft()
        y = list(str(x))
        for i, j in comb:
            copy_y = y[:]
            copy_y[i], copy_y[j] = copy_y[j], copy_y[i]
            if copy_y[0] == '0':
                continue
            nx = int(''.join(copy_y))
            if nx not in check:
                ans = max(ans, nx)
                check.add(nx)
                q.append(nx)
        lencheck -= 1
    return ans

N, K = map(int, input().split())
n = list(range(len(str(N))))
comb = list(combinations(n, 2))
q = deque()
q.append(N)
ans = 0
while K:
    ans = bfs(N)
    K -= 1
if ans == 0:
    ans = -1
print(ans)