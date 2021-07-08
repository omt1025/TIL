N, K = map(int, input().split())
package = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
result = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w = package[i][0]
        v = package[i][1]
        # 현재 물건의 무게가 새로 넣은 물건의 무게보다 작다면
        if j < w:
            result[i][j] = result[i-1][j]
        # 넣을 물건의 무게가 같거나 크면
        else:
            # 이전 가치와 현재 가치 중 큰 값을 저장 
            result[i][j] = max(v + result[i-1][j-w], result[i-1][j])

print(result[N][K])
