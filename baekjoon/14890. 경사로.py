def check(arr):
    visited = [False for _ in range(N)]
    for i in range(N-1):
        if arr[i] == arr[i + 1]:
            continue
        if abs(arr[i] - arr[i + 1]) > 1:
            return False
        if arr[i] > arr[i + 1]:
            cnt = arr[i + 1]
            for j in range(i+1, i+1+L):
                if j >= N:
                    return False
                if not arr[j] == cnt:
                    return  False
                if visited[j] == True:
                    return False
                visited[j] = True
        else:
            cnt = arr[i]
            for j in range(i, i-L, -1):
                if j < 0:
                    return False
                if not arr[j] == cnt:
                    return False
                if visited[j] == True:
                    return False
    return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    if check(board[i]):
        ans += 1

for i in range(N):
    board2 = []
    for j in range(N):
        board2.append(board[j][i])
    if check(board2):
        ans += 1
print(ans)