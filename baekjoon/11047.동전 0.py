N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
# 동전의 개수
cnt = 0
# 동전 리스트를 뒤에서부터 탐색
for i in range(N-1, -1, -1):
    # 동전의 값이 K 보다 작으면
    if K >= coin[i]:
        # 동전의 개수를 더하고
        cnt += K // coin[i]
        # 남은 액수를 K로 한다.
        K %= coin[i]
    else:
        continue
print(cnt)