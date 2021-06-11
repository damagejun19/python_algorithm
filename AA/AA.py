# import sys

# sys.stdin = open("./input.txt", "rt")
# n, k = map(int, input().split())
# cnt = 0

# for i in range(1, n + 1):
#   if n % i == 0:
#     cnt += 1

#   if cnt == k:
#     print(i)
#     break

# else:
#   print(-1)

import sys

# sys.stdin = open("./input.txt")
# T = int(input())

# for t in range(T):
#   n, s, e, k = map(int, input().split())
#   a = list(map(int, input().split()))
#   b = a[s-1:e]
#   b.sort()
#   print('#%d %d'% (t + 1, b[k-1]))

# sys.stdin = open("./input.txt")
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# res = set()

# for i in range(n):
#   for j in range(i+1, n):
#     for m in range(j+1, n):
#       sum_n = a[i] + a[j] + a[m]
#       res.add(sum_n)

# res = list(res)
# res.sort(reverse=True)
# print(res[k-1])

# sys.stdin = open("./input.txt")
# S = int(input())
# a = list(map(int, input().split()))
# ave = round( sum(a) / len(a) )
# ave_min = float('inf')

# for idx, val in enumerate(a):
#   tmp = abs(ave-val) 
  
#   if tmp < ave_min:
#     ave_min = tmp
#     score = val
#     res = idx + 1
#   elif tmp == ave_min:
#     if score < val:
#       score = val
#       res = idx + 1


# print(ave, res)


# sys.stdin = open("./input.txt")
# N, M = map(int, input().split())

# if N <= M:
#   for i in range(1+N, 1+M+1):
#     print(i, end=" ")
# else:
#   for i in range(M+1, N+1+1):
#     print(i, end=" ")
N, M = map(int, input().split())
cnt = [0] * (N + M + 1)


for i in range(1, N+1):
  for j in range(1, M+1):
    cnt[i + j] += 1


for i in range(len(cnt)):
  if cnt[i] == max(cnt):
    print(i, end=" ")



























