from _collections import deque
A, B, N, M = map(int, input().split())
# 돌다리의 위치
road = [0 for _ in range(100001)]
# 이동할 수 있는 경우의 수
move = [1, -1, A, B, -A, -B, A, B]
q = deque()
q.append(N)
while q:
    n = q.popleft()
    for i in range(8):
        # 그냥 이동하는 경우
        if i < 6:
            nn = n + move[i]
            if 0 <= nn < 100001 and road[nn] == 0:
                q.append(nn)
                road[nn] += road[n] + 1
        # 힘을 모아서 점프하는 경우
        else:
            nn = n * move[i]
            if 0 <= nn < 100001 and road[nn] == 0:
                q.append(nn)
                road[nn] += road[n] + 1
print(road[M])