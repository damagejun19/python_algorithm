n, k = map(int, input().split())
n_list = list(map(int, input().split()))
a = set()

for i in range(n):
  for j in range(i+1, n):
    for s in range(j+1, n):
      hap = n_list[i] + n_list[j] + n_list[s]
      a.add(hap)
      
a = list(a)
a.sort(reverse=True)
print(a[k - 1])