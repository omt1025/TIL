from _collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
visit = [[0] * W for _ in range(H)]
dr = [-1, 0, 1, 0, -1, -1, 1, 1]
dc = [0, -1, 0, 1, -1, 1, -1, 1]
q = deque()
for i in range(H):
    for j in range(W):
        if arr[i][j] == '.':
            arr[i][j] = 0
            q.append((i, j))
        else:
            arr[i][j] = int(arr[i][j])
ans = 0
while q:
    r, c = q.popleft()
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < H and 0 <= nc < W:
            if arr[nr][nc]:
                arr[nr][nc] -= 1
                if arr[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    ans = max(ans, visit[nr][nc])
                    q.append((nr, nc))
print(ans)
'''
ans = 0
q = deque()

while True:
    for i in range(H):
        for j in range(W):
            if arr[i][j] != '.':
                num = int(arr[i][j])
                if num < 9:
                    r, c = i, j
                    cnt = 0
                    for k in range(8):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < H and 0 <= nc < W:
                            if arr[nr][nc] == '.':
                                cnt += 1
                    if cnt >= num:
                        q.append((i, j))
    if len(q) == 0:
        break
    else:
        while q:
            x, y = q.popleft()
            arr[x][y] = '.'
    ans += 1
print(ans)
'''
