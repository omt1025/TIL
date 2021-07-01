from itertools import combinations
A = float(input()) / 100
B = float(input()) / 100
# 18이하의 소수 2, 3, 5, 7, 11, 13, 17로 7가지
num = [2, 3, 5, 7, 11, 13, 17]
goalA = 0
goalB = 0
for i in range(19):
    if not i in num:
        goalA += len(list(combinations(range(18), i))) * (A ** i) * ((1-A) ** (18-i))
        goalB += len(list(combinations(range(18), i))) * (B ** i) * ((1-B) ** (18-i))
ans = 1 - goalA*goalB
print(ans)