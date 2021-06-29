import sys
from _collections import deque

I = sys.stdin.readline
M, N = map(int, I().split())
Miro = [list(map(int, I().strip())) for _ in range(N)]
cnt = [[-1] * M for _ in range(N)]
q = deque()
q.append((0, 0))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
cnt[0][0] = 0
while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if cnt[nr][nc] == - 1:
            if Miro[nr][nc] == 1:
                q.append((nr, nc))
                cnt[nr][nc] = cnt[r][c] + 1
            else:
                q.appendleft((nr, nc))
                cnt[nr][nc] = cnt[r][c]
print(cnt[N-1][M-1])
