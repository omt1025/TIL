N = int(input())
P = list(map(int, input().split()))
# 최솟값은 시간이 적은 순서대로 줄을 섰을 때 나온다.
P.sort()
# 각 사람마다 걸리는 시간을 구한 후
for i in range(N-1):
    P[i+1] += P[i]
# 다 더한 값을 출력
print(sum(P))