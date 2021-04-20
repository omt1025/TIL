dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs(r, c):
    cnt = 1
    q = set([(r, c, arr[r][c])])
    while q:
        r, c, ans = q.pop()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if not arr[nr][nc] in ans:
                q.add((nr, nc, ans + arr[nr][nc]))
                cnt = max(cnt, len(ans)+1)

    return cnt

R, C = map(int, input().split())
arr = []
for _ in range(R):
    temp = []
    for x in input():
        temp.append(x)
    arr.append(temp)
ans = bfs(0, 0)
print(ans)