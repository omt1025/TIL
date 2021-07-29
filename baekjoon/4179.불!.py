from _collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
miro = [list(input()) for _ in range(R)]
visit = [[-1] * C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
q = deque()
q2 = deque()
ans = -1
for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            q.append((i, j, 1))
            visit[i][j] = 0
        elif miro[i][j] == 'F':
            q2.append((i, j))
            visit[i][j] = 0

while q2:
    r2, c2 = q2.popleft()
    for i in range(4):
        nr2, nc2 = r2 + dr[i], c2 + dc[i]
        if 0 <= nr2 < R and 0 <= nc2 < C:
            if miro[nr2][nc2] == "." and visit[nr2][nc2] == -1:
                visit[nr2][nc2] = visit[r2][c2] + 1
                q2.append((nr2, nc2))
while q:
    r, c, time = q.popleft()
    if r == 0 or r == R - 1 or c == 0 or c == C - 1:
        ans = time
        break
    for j in range(4):
        nr, nc = r + dr[j], c + dc[j]
        if 0 <= nr < R and 0 <= nc < C:
            if visit[nr][nc] > time and miro[nr][nc] == ".":
                q.append((nr, nc, time + 1))
                visit[nr][nc] = time
if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans)