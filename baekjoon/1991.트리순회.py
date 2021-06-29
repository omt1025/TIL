N = int(input())
node = [list(input().split()) for _ in range(N)]
tree = {}
ans1 = ''
ans2 = ''
ans3 = ''
for i in range(N):
    x, y, z = node[i]
    tree[x] = [y, z]
# 전위 순회
def pre(n):
    global ans1
    if n != '.':
        ans1 += n
        pre(tree[n][0])
        pre(tree[n][1])
# 중위 순회
def mid(n):
    global ans2
    if n != '.':
        mid(tree[n][0])
        ans2 += n
        mid(tree[n][1])
# 후위 순회
def post(n):
    global ans3
    if n != '.':
        post(tree[n][0])
        post(tree[n][1])
        ans3 += n

pre('A')
mid('A')
post('A')
print(ans1)
print(ans2)
print(ans3)