from collections import deque
import copy

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c][0] = 1
    while q:
        r, c, k = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 0 and visited[nr][nc][k] == -1:
                visited[nr][nc][k] = visited[r][c][k] + 1
                q.append((nr, nc, k))
            elif k == 0 and arr[nr][nc] == 1 and visited[nr][nc][k+1] == -1:
                visited[nr][nc][k+1] = visited[r][c][k] + 1
                q.append([nr, nc, k+1])

    return

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
bfs(0, 0)
ans1, ans2 = visited[N-1][M-1][0], visited[N-1][M-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))
