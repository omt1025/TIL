from _collections import deque

N, R, D, X, Y = map(int, input().split())
Top = [list(map(int, input().split())) for _ in range(N)]
game = [[0] * 11 for _ in range(11)]
for i in range(N):
    game[Top[i][0]][Top[i][1]] = D
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for x, y in Top:
    q = deque()
    m = 0
    q.append((x, y, m))
    visit = [[0] * 11 for _ in range(11)]
    d = game[x][y]
    while q:
        r, c, mm = q.popleft()
        visit[r][c] = 1
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr <= 10 and 0 <= nc <= 10:
                if visit[nr][nc]:
                    continue
                if mm <= R:
                    if game[nr][nc]:
                        game[nr][nc] += d / 2
                    q.append((nr, nc, mm+1))
print(game)