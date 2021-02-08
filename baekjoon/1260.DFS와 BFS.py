# https://www.acmicpc.net/problem/1260
import sys
sys.setrecursionlimit(99999)

def dfs(n):
    print(n, end=' ')
    visited1[n] = 1
    for i in range(N+1):
        if p[n][i] and visited1[i] == 0:
            dfs(i)

def bfs(n):
    visited2[n] = 1
    qe = []
    qe.append(n)
    while qe:
        x = qe.pop(0)
        print(x, end=' ')
        q[x].sort()
        for i in q[x]:
            if visited2[i] == 0:
                visited2[i] = 1
                qe.append(i)
    return

N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
p = [[0] * (N+1) for _ in range(N+1)]
q = [[] * (N+1) for _ in range(N+1)]
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)
for r in arr:
    s, e = r[0], r[1]
    p[s][e] = 1
    p[e][s] = 1
    q[s].append(e)
    q[e].append(s)
dfs(V)
print()
bfs(V)