N = int(input())
ans = 0
S = str(N)
NS = list(S)
print(NS)
L = len(S)
if N + 1 < 10:
    ans = N + 1
elif len(S):
    if len(S) % 2 == 0:
        cnt = 0
        for i in range(L//2+1):
            if S[i] == S[L-1-i]:
                cnt += 1
        if cnt == L // 2:
            print(cnt)
            ans = N
print(ans)