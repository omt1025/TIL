for tc in range(1, int(input())+1):
    K = int(input())
    files = list(map(int, input().split()))

    check = [[0]*K for _ in range(K)]
    for i in range(K-1):
        check[i][i+1] = files[i] + files[i+1]
        for j in range(i+2, K):
            check[i][j] = check[i][j-1] + files[j]
    for x in range(2, K):
        for y in range(K-x):
            z = x+y
            mini = [check[y][K] + check[K+1][z] for K in range(y, z)]
            check[y][z] += min(mini)
    print(check[0][K-1])