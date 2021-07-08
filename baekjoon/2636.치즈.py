from _collections import deque
import sys

def bfs():
    global cnt
    visited = [[0] * M for _ in range(N)]
    air = deque()
    air.append((0, 0))
    visited[0][0] = 1
    # 공기에 접한 부분만 탐색하면 된다.
    while air:
        r, c = air.popleft()
        for x in range(4):
            nr, nc = r + dr[x], c + dc[x]
            # 공기일 때
            if visited[nr][nc] == 0 and board[nr][nc] == 0:
                visited[nr][nc] = 1
                air.append((nr, nc))
            # 공기에 접한 치즈일 때
            elif board[nr][nc] == 1:
                cnt += 1
                visited[nr][nc] = 1
                board[nr][nc] = 0

read = sys.stdin.readline
N, M = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(N)]
h, c = 0, 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while True:
    cnt = 0
    bfs()
    # 치즈가 하나도 남지 않았을 때 반복문을 종료한다.
    if cnt == 0:
        break
    # 치즈가 남아있으면 시간과 남은 치즈 개수를 저장한다.
    c = cnt
    h += 1
print(h)
print(c)