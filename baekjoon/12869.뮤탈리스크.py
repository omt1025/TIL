from _collections import deque
from itertools import permutations

N = int(input())
H = list(map(int, input().split()))
# scv는 3마리로 고정시키는 것이 계산이 편함
while len(H) < 3:
    H.append(0)
# 방문 처리 배열 생성 최대 체력은 60이라 범위는 61까지
hp = [[[False] * 61 for _ in range(61)] for _ in range(61)]
# 데미지를 줄 수 있는 경우의 수를 순열로 구함
D = list(permutations([9, 3, 1], 3))
q = deque()
q.append([H, 0])
def bfs():
    while q:
        # 현재 scv들의 체력과 공격 횟수
        h, cnt = q.popleft()
        # 체력이 모두 없으면 cnt 리턴
        if h[0] <= 0 and h[1] <= 0 and h[2] <= 0:
            return cnt
        # 이미 카운팅 한 체력일 경우 continue
        if hp[h[0]][h[1]][h[2]]:
            continue
        # 방문처리
        hp[h[0]][h[1]][h[2]] = True
        # 체력이 닳았을 때 0이하면 0으로 저장
        for d in D:
            a, b, c = max(0, h[0] - d[0]), max(0, h[1] - d[1]), max(0, h[2] - d[2])
            q.append([[a, b, c], cnt+1])
print(bfs())
