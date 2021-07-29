from itertools import permutations
N = int(input())
num = [list(input()) for _ in range(N)]
check = list(permutations(range(10), 10))
print(check)
'''
897
978
1875
'''