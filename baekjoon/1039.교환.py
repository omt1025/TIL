# https://www.acmicpc.net/problem/1039
def check1(n, l):
    cnt = 0
    while cnt < int(K):
        temp = cnt
        for i in range(l-1):
            start = n[i]
            idx = i
            for j in range(l-1, i-1, -1):
                if start < n[j]:
                    start = n[j]
                    idx = j
            if idx != i:
                n[i], n[idx] = n[idx], n[i]
                cnt += 1
            if cnt == int(K):
                break
        if temp == cnt:
            break
    if cnt < int(K):
        if n != set(n):
            while cnt < int(K):
                n[l-2], n[l-1] = n[l-1], n[l-2]
                cnt += 1
    ans = 0
    for num in n:
        ans += num * (10 ** (l - 1))
        l -= 1
    return ans

def check2(n, l):
    cnt = 0
    while cnt < int(K):
        temp = cnt
        for i in range(l-1):
            start = n[i]
            idx = i
            for j in range(i+1, l):
                if start < n[j]:
                    start = n[j]
                    idx = j
            if idx != i:
                n[i], n[idx] = n[idx], n[i]
                cnt += 1
            if cnt == int(K):
                break
        if temp == cnt:
            break
    if cnt < int(K):
        if n != set(n):
            while cnt < int(K):
                n[l-2], n[l-1] = n[l-1], n[l-2]
                cnt += 1
    ans = 0
    for num in n:
        ans += num * (10 ** (l - 1))
        l -= 1
    return ans

N, K = map(str, input().split())
n = list(map(int, N))
l = len(n)
n1, n2 = n[:], n[:]
if l == 1 or (l == 2 and n[1] == 0):
    print(-1)
else:
    ans = 0
    a1, a2 = check1(n1, l), check2(n2, l)
    if a1 > a2:
        ans = a1
    else:
        ans = a2
    print(ans)