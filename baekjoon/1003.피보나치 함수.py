for tc in range(int(input())):
    N = int(input())
    # 0과 1이 몇번 사용됐는지만 알면 되니깐 column은 2
    ans = [[0] * 2 for _ in range(N+1)]
    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        ans[0][0] = 1
        ans[1][1] = 1
        # 피보나치대로 -2 -1을 더한다.
        for i in range(2, N+1):
            ans[i][0] = ans[i-1][0] + ans[i-2][0]
            ans[i][1] = ans[i-1][1] + ans[i-2][1]
        for j in ans[N]:
            print(j, end=' ')
        print()
