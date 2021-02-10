# https://www.acmicpc.net/problem/11660
"""
시간초과가 계속 났던 문제
입력이 많을 때는 sys이용하자
3중 for문은 시간 복잡도가 크기 때문에 dp 사용해야함
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = arr[i-1][j-1] + DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1]
for row in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])
