def SOD(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += i
    return total

n = int(input())
ans = 0
if n == 1:
    print(0)
else:
    for i in range(2, n+1):
        ans += SOD(i) - i - 1
    print(ans%1000000)
