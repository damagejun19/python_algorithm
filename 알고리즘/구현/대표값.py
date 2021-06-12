n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a) / n)
min = 214000000

for idx, val in enumerate(a):
  tmp = abs(ave - val)
  if tmp < min:
    min = tmp
    score = val
    res = idx + 1
  elif tmp == min:
    if val > score:
      score = val
      res = idx + 1
print(ave, res)

