S, K = map(int, input().split())
X = S // K
Y = S % K
ans = (X ** (K - Y)) * ((X+1) ** Y)
print(ans)