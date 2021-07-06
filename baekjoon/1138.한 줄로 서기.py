N = int(input())
people = list(map(int, input().split()))
ans = [0] * len(people)
for i in range(N):
    check = 0
    if i == N-1:
        for k in range(N):
            if ans[k] == 0:
                ans[k] = i+1
                break
    else:
        for j in range(N):
            if ans[j] == 0 and check < people[i]:
                check += 1
            elif ans[j] == 0 and check == people[i]:
                ans[j] = i+1
                break
for num in ans:
    print(num, end=' ')
print()
