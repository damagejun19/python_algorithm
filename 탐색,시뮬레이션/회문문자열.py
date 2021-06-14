n = int(input())

for i in range(n):
  a = input()
  a = a.lower()
  for j in range(len(a) // 2):
    if a[j] != a[-1 -j]:
      print("#%d NO" % (i + 1))
      break
  else:
    print("#%d Yes" % (i + 1))