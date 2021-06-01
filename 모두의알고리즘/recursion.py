# 재귀를 이용한 덧셈


def sum_n(n):
    if n <= 1:
        return 1
    return n + sum_n(n-1) 

# 재귀를 이용한 최댓값 찾기


def find_max(a, n):
    print(a, n)
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n - 1)
    if max_n_1 > a[n - 1]:
        return max_n_1
    else:
        return a[n - 1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))

# 재귀호출을 이요한 피보나치 수열


def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(7))




