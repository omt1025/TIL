# from _collections import deque
import sys
sys.setrecursionlimit(1000000000)
N = int(input())
check = [[[-1] * 3 for _ in range(2)] for _ in range(N+1)]
def dfs(day, late, abs):
    if late == 2 or abs == 3:
        return 0
    if day == N:
        return 1
    if check[day][late][abs] == -1:
        attend = dfs(day + 1, late, 0) + dfs(day + 1, late + 1, 0) + dfs(day + 1, late, abs + 1)
        check[day][late][abs] = attend

        return attend
    else:
        return check[day][late][abs]

print(dfs(0, 0, 0) % 1000000)
#
# q = deque()
# q.append((0, 0, 0, 0, 0))
# ans = 0
# while q:
#     O, L, A, CA, n = q.popleft()
#     if n < N:
#         q.append((O+1, L, 0, 0, n+1))
#         if L+1 != 2:
#             q.append((O, L+1, 0, 0, n+1))
#         if CA == 1:
#             if A + 1 < 3:
#                 q.append((O, L, A+1, 1, n+1))
#         else:
#             q.append((O, L, A+1, 1, n+1))
#     else:
#         break
# print(len(q)+1)
