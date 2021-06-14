a = input()
res = 0
cnt = 0

for i in a:
  if i.isdecimal():
    res  = res * 10 + int(i)

for j in range(1, res + 1):
  if res % j == 0:
    cnt += 1

print(res, cnt, sep="\n")