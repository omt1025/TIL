from _collections import deque
R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[0] * C for _ in range(R)]
# 양, 늑대
ans = [0] * 2
# 필드 탐색
for i in range(R):
    for j in range(C):
        # 방문하지 않고 울타리가 아닐 경우 탐색
        if visited[i][j] == 0 and field[i][j] != '#':
            # 양, 늑대 마릿수 체크
            sheep, wolf = 0, 0
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            # bfs 탐색
            while q:
                r, c = q.popleft()
                # 양일 경우 sheep에 1 추가
                if field[r][c] == 'o':
                    sheep += 1
                # 늑대일 경우 wolf에 1 추가
                elif field[r][c] == 'v':
                    wolf += 1
                # 사방 탐색
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < R and 0 < nc < C:
                        if field[nr][nc] != '#' and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
            # 양이 늑대보다 많을 경우 양의 마릿수만 추가
            if sheep > wolf:
                ans[0] += sheep
            # 이외에는 늑대 마릿수만 추가
            else:
                ans[1] += wolf
print(ans[0], ans[1])
