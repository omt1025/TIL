from _collections import deque
import sys
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
dx = [-1, -2, 1, 2, -1, -2, 1, 2]
dy = [-2, -1, -2, -1, 2, 1, 2, 1]
def bfs():
    q = deque()
    q.append((0, 0, K))
    visited = [[[0] * 31 for _ in range(W)] for _ in range(H)]
    while q:
        r, c, k = q.popleft()
        if r == H-1 and c == W-1: return visited[r][c][k]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == 0 and visited[nr][nc][k] == 0:
                    visited[nr][nc][k] = visited[r][c][k] + 1
                    q.append((nr, nc, k))
        if k > 0:
            for i in range(8):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if arr[nr][nc] == 0 and visited[nr][nc][k-1] == 0:
                        visited[nr][nc][k-1] = visited[r][c][k] + 1
                        q.append((nr, nc, k-1))
    return -1

print(bfs())