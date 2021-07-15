from _collections import deque
import sys

def bfs(x, y):
    # 타일 모양대로 탐색하려면 짝수행, 홀수행의 탐색 범위가 달라지게 된다.
    o_dx = [-1, 0, 1, -1, 0, 1]
    o_dy = [1, 1, 1, 0, -1, 0]
    e_dx = [-1, 0, 1, 1, 0, -1]
    e_dy = [0, 1, 0, -1, -1, -1]
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        # 홀수 행일 때 탐색 방법
        if x % 2 == 1:
            dx, dy = o_dx, o_dy
        # 짝수 행일 때 탐색 방법
        else:
            dx, dy = e_dx, e_dy
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    # 자신을 기준으로 오른쪽 타일을 탐색할 땐 타일 내에서 오른쪽 조각으로 탐색
                    if i <= 2:
                        if Domino[x][y][1] == Domino[nx][ny][0]:
                            visited[nx][ny] = visited[x][y] + 1
                            move[nx][ny] = [x, y]
                            q.append([nx, ny])
                    # 왼쪽 타일을 탐색할 땐 타일 내에서 왼쪽 조각으로 탐색
                    else:
                        if Domino[x][y][0] == Domino[nx][ny][1]:
                            visited[nx][ny] = visited[x][y] + 1
                            move[nx][ny] = [x, y]
                            q.append([nx, ny])

read = sys.stdin.readline
N = int(read())
Domino = [[[[] for _ in range(2)] for _ in range(N)] for _ in range(N)]
for i in range(N):
    # 짝수 행 입력받기
    if i % 2 == 0:
        for j in range(N):
            x, y = map(int, read().split())
            Domino[i][j] = [x, y]
    # 홀수 행 입력받기
    else:
        for j in range(N-1):
            x, y = map(int, read().split())
            Domino[i][j] = [x, y]
# 이동 배열 만들기
tile = [[[] for _ in range(N)] for _ in range(N)]
# 타일 번호
num = 0
# 타일 번호 새기기
for i in range(N):
    for j in range(N):
        # 홀수 행 마지막열은 비워두기
        if i % 2 == 1 and j == N - 1:
            continue
        num += 1
        tile[i][j] = num
q = deque()
visited = [[0] * N for _ in range(N)]
move = [[[] for _ in range(N)] for _ in range(N)]
bfs(0, 0)
ans = []
temp = False
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        # 마지막 줄의 마지막 타일이나 번호가 큰 타일로 이동하면 된다.
        if visited[i][j]:
            # 이동 횟수
            print(visited[i][j])
            ans.append(tile[i][j])
            x, y = i, j
            # 도착 지점부터 시작 지점까지의 타일을 ans 배열에 저장
            while x > 0 or y > 0:
                nx, ny = move[x][y]
                ans.append(tile[nx][ny])
                x, y = nx, ny
            temp = True
            break
    if temp:
        break
# 배열을 뒤집고
ans.reverse()
# 출력
for a in ans:
    print(a, end=' ')