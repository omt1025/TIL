from _collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
h, c = 0, 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while True:
    h += 1
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    air = deque()
    air.append((0, 0))
    while air:
        r, c = air.popleft()
        visited[r][c] = 1
        for x in range(4):
            nr, nc = r + dr[x], c + dc[x]
            if visited[nr][nc] == 0 and board[nr][nc] == 0:
                air.append((nr, nc))
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                melt = False
                for k in range(4):
                    ni, nj = i + dr[k], j + dc[k]
                    if board[ni][nj] == 0 and visited[ni][nj] == 1:
                        melt = True
                        break
                if melt:
                    q.append((i, j))
                else:
                    cnt += 1
    while q:
        r, c = q.popleft()
        board[r][c] = 0
    if cnt == 0:
        break
    c = cnt
print(h)
print(c-1)