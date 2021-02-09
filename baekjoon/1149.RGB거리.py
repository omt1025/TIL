# https://www.acmicpc.net/problem/1149
"""
처음에 재귀로 풀어서 망했다. 이런 문제는 DP로 풀기
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 배열에 이전 집을 칠하는데 드는 최소 비용을 더해간다.
for i in range(1, N):
    arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
    arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
    arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])
# 마지막 행에서 최솟값을 ans에 저장
ans = min(arr[N-1][0], arr[N-1][1], arr[N-1][2])
print(ans)