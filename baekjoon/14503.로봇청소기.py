# https://www.acmicpc.net/problem/14503
"""
보자마자 dfs로 풀어야한다고 생각이 나야 된다.
"""
import sys
input = sys.stdin.readline

# 왼쪽부터 돌아가면서 탐색
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def dfs(r, c, d):
    global ans
    # 갈 수 있는 곳이면
    if arr[r][c] == 0:
        # 청소한 것으로 처리한 후
        arr[r][c] = 2
        # 청소한 칸수에 + 1
        ans += 1
    # 사방탐색
    for i in range(4):
        # 지금 바라보고 있는 방향에서 왼쪽이으로 3을 더하고 4보다 커질 경우를 처리하기 위해 4로 나눈 나머지를 저장
        nd = (d + 3) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        if arr[nr][nc] == 0:
            dfs(nr, nc, nd)
            return
        # 네 방향을 다 탐색한 후 보는 방향 처리
        d = nd
    # 뒤로 후진
    nd = (d + 2) % 4
    nr, nc = r + dr[nd], c + dc[nd]
    # 뒤가 벽이면 리턴
    if arr[nr][nc] == 1:
        return
    # 보는 방향을 유지하면서 재귀
    dfs(nr, nc, d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(r, c, d)
print(ans)

