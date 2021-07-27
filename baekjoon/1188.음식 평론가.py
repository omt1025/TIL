def dfs(x, y):
    if x % y == 0:
        return y
    return dfs(y, x % y)
N, M = map(int, input().split())
print(M - dfs(N, M))