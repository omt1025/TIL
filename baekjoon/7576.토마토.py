# https://www.acmicpc.net/problem/7576

from _collections import deque
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 큐 생성
q = deque()
# 걸린 시간을 저장할 배열
date = [[0] * M for _ in range(N)]
# 익은 토마토를 큐에 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
# 사방탐색
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
# 큐가 빌 때까지 반복
while q:
    # 큐에서 가장 왼쪽 요소를 꺼냄
    r, c = q.popleft()
    # 사방탐색
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        # 인덱스를 벗어나면 continue
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        # 익지 않은 토마토이면
        if arr[nr][nc] == 0:
            # 익은 토마토로 바꾸고
            arr[nr][nc] = 1
            # 이전 토마토가 익는데 걸린 시간에 1을 더한 값을 저장
            date[nr][nc] = date[r][c] + 1
            # 큐에 저장
            q.append((nr, nc))
ans = 0
# 익는데 가장 오래 걸린 기간을 ans에 저장
for row in date:
    max_row = max(row)
    if ans < max_row:
        ans = max_row
# 익지 않은 토마토가 있다면 ans에 -1 저장
for row in arr:
    if 0 in row:
        ans = -1
        break

print(ans)

