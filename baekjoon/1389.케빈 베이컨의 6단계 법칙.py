def check(n, m):
    global cnt
    # 확인할 친구이면
    if n == m:
        # temp 배열에 cnt를 저장하고 리턴
        temp.append(cnt)
        return
    # 지정한 사람의 친구를 탐색
    for i in range(N+1):
        # 친구 관계이고 방문처리가 안되어 있으면
        if friends[n][i] and visited[i] == 0:
            # 1단계를 더한후 방문처리
            cnt += 1
            visited[i] = 1
            # 재귀
            check(i, m)
            # 다른 경우를 탐색하기 위해 단계를 낮추고 방문처리를 0으로
            cnt -= 1
            visited[i] = 0

# N: 유저의 수, M: 친구 관계의 수
N, M = map(int, input().split())
# 친구 관계
arr = [list(map(int, input().split())) for _ in range(M)]
# 2차원 배열로 친구관계를 저장
friends = [[0] * (N+1) for _ in range(N+1)]
# 양방향 배열로 저장
for i in range(M):
    s, e = arr[i][0], arr[i][1]
    friends[s][e] = 1
    friends[e][s] = 1
# 친구 관계의 단계를 저장할 배열 생성
result = [[0] * (N+1) for _ in range(N+1)]
# 몇단계를 거치더라도 친구 관계는 양방향 배열이므로 한 방향만 탐색하면 된다. 
for j in range(1, N+1):
    for k in range(j+1, N+1):
        # 방문 처리를 할 배열 생성
        visited = [0] * (N+1)
        # 친구 관계의 단계를 담을 변수 생성
        cnt = 0
        # cnt를 담을 배열 생성
        temp = []
        # 탐색할 사람을 방문처리
        visited[j] = 1
        # check 함수 실행
        check(j, k)
        # 결과 배열에 단계의 최솟값 저장
        result[j][k] = min(temp)
        result[k][j] = min(temp)
# 케빈 베이컨의 수가 작은 사람을 담을 변수
ans = 0
# 케빈 베이컨의 수를 담을 변수
total = 9999999
for l in range(1, N+1):
    # 케빈 베이컨의 수가 작으면
    if sum(result[l]) < total:
        # 결과에 저장
        total = sum(result[l])
        ans = l
print(ans)
