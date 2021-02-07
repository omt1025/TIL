# https://www.acmicpc.net/problem/1012
from _collections import deque
# bfs 함수
def bfs(a, b):
    # 사방탐색
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    # 큐 생성
    q = deque()
    q.append((a, b))
    # 방문처리
    visited[a][b] = 1
    # 큐가 빌 때까지 실행
    while q:
        # pop
        r, c = q.popleft()
        # 사방탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc]:
                continue
            # 배추일 경우에 방문처리 후 큐에 추가
            if field[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    # 밭 배열을 만들어줌
    field = [[0] * M for _ in range(N)]
    # 밭의 배추 위치를 1로 만들어줌
    for i in range(K):
        r, c = arr[i][1], arr[i][0]
        field[r][c] = 1
    # 방문 배열 생성
    visited = [[0] * M for _ in range(N)]
    # 배추흰지렁이 마리수를 저장할 변수 생성
    cnt = 0
    # bfs 함수 실행
    for j in range(N):
        for k in range(M):
            if visited[j][k] == 0 and field[j][k]:
                bfs(j, k)
                cnt += 1
    # 결과
    print(cnt)