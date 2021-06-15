n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.append([0] * n)
a.insert(0, [0] * n)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

for i in a:
  i.append(0)
  i.insert(0, 0)

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
      cnt += 1

print(cnt)