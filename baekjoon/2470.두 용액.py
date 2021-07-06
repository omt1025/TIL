import sys
read = sys.stdin.readline

N = int(read())
l = list(map(int, read().split()))
l.sort()
ans = [0] * 2
mix = float('inf')
# 이분 탐색을 위해 시작점과 끝점을 설정한다.
s, e = 0, len(l)-1
while s < e:
    # 한 종류만 주어지는 경우가 있기 때문에 범위를 설정한다.
    if s >= len(l)-1 or e <= 0:
        break
    # 두 용액을 섞은 값
    result = l[s] + l[e]
    # 섞은 값의 절댓값이 mix값보다 작으면
    if abs(result) < mix:
        # mix에 결과를 저장하고
        mix = abs(result)
        # ans에 넣은 용액을 저장한다.
        ans[0], ans[1] = l[s], l[e]
    # 섞은 값이 양수이면 끝 지점을 당기고
    if result >= 0:
        e -= 1
    # 아닐 경우 시작 지점을 민다.
    else:
        s += 1

print(ans[0], ans[1])